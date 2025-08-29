import random
from datetime import timedelta

import numpy as np
import pandas as pd

from dev.types.extended_position_data import PolarData, NedData, ExtendedPositionData
from dev.types.sensor_data import SensorData


def sample_path_in_sensor_frame(path_local_ned: NedData, sensor_data: SensorData) -> ExtendedPositionData:
    # Vector from sensor to each path position
    sample_dt = 1 / sensor_data.rate
    first_timestamp = path_local_ned.t[0] + timedelta(seconds=random.uniform(0, sample_dt))
    sensor_timestamps = pd.date_range(start=first_timestamp, end=path_local_ned.t[-1],
                                      freq=timedelta(seconds=sample_dt)).values

    t_ref = path_local_ned.t[0]
    path_time_sec = (np.array(path_local_ned.t, dtype="datetime64[ns]") - np.datetime64(t_ref)) / np.timedelta64(1, "s")
    interpolate_timestamps = (np.array(sensor_timestamps, dtype="datetime64[ns]") - np.datetime64(t_ref)) / np.timedelta64(1, "s")
    x_measured = np.interp(interpolate_timestamps, path_time_sec, path_local_ned.x)
    y_measured = np.interp(interpolate_timestamps, path_time_sec, path_local_ned.y)
    z_measured = np.interp(interpolate_timestamps, path_time_sec, path_local_ned.z)

    drone_coordinates = np.vstack([x_measured, y_measured, z_measured]).T
    vectors = drone_coordinates - np.array([sensor_data.x, sensor_data.y, sensor_data.z])

    # Distances (range)
    ranges = np.linalg.norm(vectors, axis=1)

    # Azimuth (angle in XY plane)
    azimuth = np.arctan2(vectors[:, 1], vectors[:, 0])

    # Elevation (angle from XY plane upward)
    elevation = np.arctan2(vectors[:, 2], np.linalg.norm(vectors[:, :2], axis=1))
    return ExtendedPositionData(t=sensor_timestamps,
                                r=ranges, az=azimuth, el=elevation,
                                x=x_measured, y=y_measured, z=z_measured)


def polar_to_ned(polar: PolarData) -> NedData:
    # Convert spherical to cartesian
    return NedData(
        t=polar.t,
        x=polar.r * np.cos(polar.el) * np.cos(polar.az),
        y=polar.r * np.cos(polar.el) * np.sin(polar.az),
        z=polar.r * np.sin(polar.el)
    )
