import numpy as np

from dev.types.extended_position_data import PolarData, ExtendedPositionData, NedData
from dev.types.sensor_data import SensorData
from dev.utilities.position import polar_to_ned


def add_noise_to_sensor_samples(sensor: SensorData, los: ExtendedPositionData):
    num_points = len(los.r)

    noisy_los_sensor_polar = PolarData(
        t=los.t,
        r=los.r + np.random.normal(0, sensor.rng_noise_std, num_points),
        az=los.az + np.random.normal(0, sensor.az_noise_std, num_points),
        el=los.el + np.random.normal(0, sensor.el_noise_std, num_points))

    noisy_los_sensor_ned = polar_to_ned(noisy_los_sensor_polar)
    drone_coordinates = np.vstack([noisy_los_sensor_ned.x, noisy_los_sensor_ned.y, noisy_los_sensor_ned.z]).T
    temp = drone_coordinates + np.array([sensor.x, sensor.y, sensor.z])
    noisy_los_local_ned = NedData(t=los.t, x=temp[:, 0], y=temp[:, 1], z=temp[:, 2])
    plots = ExtendedPositionData.from_parts(ned=noisy_los_local_ned, polar=noisy_los_sensor_polar)

    return plots
