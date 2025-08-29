import numpy as np

from dev.types.extended_position_data import PolarData, NedData
from dev.types.sensor_data import SensorData


def calc_polar_los(path_ned_data: NedData, radar_data: SensorData) -> PolarData:
    # Vector from sensor to each path position
    drone_coordinates = np.vstack([path_ned_data.x, path_ned_data.y, path_ned_data.z]).T
    vectors = drone_coordinates - np.array([radar_data.x, radar_data.y, radar_data.z])

    # Distances (range)
    ranges = np.linalg.norm(vectors, axis=1)

    # Azimuth (angle in XY plane)
    azimuth = np.arctan2(vectors[:, 1], vectors[:, 0])

    # Elevation (angle from XY plane upward)
    elevation = np.arctan2(vectors[:, 2], np.linalg.norm(vectors[:, :2], axis=1))
    return PolarData(t=path_ned_data.t, r=ranges, az=azimuth, el=elevation)


def polar_to_ned(polar: PolarData) -> NedData:
    # Convert spherical to cartesian
    return NedData(
        t=polar.t,
        x=polar.r * np.cos(polar.el) * np.cos(polar.az),
        y=polar.r * np.cos(polar.el) * np.sin(polar.az),
        z=polar.r * np.sin(polar.el)
    )
