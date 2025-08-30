import random
from datetime import timedelta

import numpy as np
import pandas as pd

from dev.types.drone_data import DroneData
from dev.types.extended_position_data import PolarData, NedData, ExtendedPathData, GeoPathData
from dev.types.sensor_data import SensorData
import pymap3d as pm


def get_time_stamps(rate, time_vector):
    sample_dt = 1 / rate
    first_timestamp = time_vector[0] + timedelta(seconds=random.uniform(0, sample_dt))
    sensor_timestamps_datetime = pd.date_range(start=first_timestamp, end=time_vector[-1],
                                               freq=timedelta(seconds=sample_dt)).to_list()

    t_ref = time_vector[0]
    original_timestamp = (np.array(time_vector, dtype="datetime64[ns]") - np.datetime64(t_ref)) / np.timedelta64(1,
                                                                                                                  "s")
    sensor_timestamps = ((np.array(sensor_timestamps_datetime, dtype="datetime64[ns]") - np.datetime64(t_ref))
                         / np.timedelta64(1, "s"))

    return original_timestamp, sensor_timestamps, sensor_timestamps_datetime


def sample_path_in_sensor_frame(drone_data: DroneData, sensor_data: SensorData) -> ExtendedPathData:
    original_timestamp, sensor_timestamps, sensor_timestamps_datetime = get_time_stamps(sensor_data.rate, drone_data.t)

    latitude_measured = np.interp(sensor_timestamps, original_timestamp, drone_data.lla.latitude)
    longitude_measured = np.interp(sensor_timestamps, original_timestamp, drone_data.lla.longitude)
    altitude_measured = np.interp(sensor_timestamps, original_timestamp, drone_data.lla.altitude)

    # Vector from sensor to each path position
    lla0 = sensor_data.position
    north, east, down = pm.geodetic2ned(lat=latitude_measured, lon=longitude_measured, h=altitude_measured,
                                        lat0=lla0.latitude, lon0=lla0.longitude, h0=lla0.altitude)
    drone_coordinates = np.vstack([north, east, down]).T

    # Distances (range)
    ranges = np.linalg.norm(drone_coordinates, axis=1)

    # Azimuth (angle in XY plane)
    azimuth = np.arctan2(drone_coordinates[:, 1], drone_coordinates[:, 0])

    # Elevation (angle from XY plane upward)
    elevation = np.arctan2(drone_coordinates[:, 2], np.linalg.norm(drone_coordinates[:, :2], axis=1))

    return ExtendedPathData(
        t=sensor_timestamps_datetime, polar=PolarData(r=ranges, az=azimuth, el=elevation),
        ned=NedData(north=north, east=east, down=down, origin=sensor_data.position),
        llh=GeoPathData(latitude=latitude_measured, longitude=longitude_measured, altitude=altitude_measured))


def polar_to_ned(polar: PolarData) -> NedData:
    # Convert spherical to cartesian
    return NedData(
        north=polar.r * np.cos(polar.el) * np.cos(polar.az),
        east=polar.r * np.cos(polar.el) * np.sin(polar.az),
        down=polar.r * np.sin(polar.el),
        origin=polar.origin
    )
