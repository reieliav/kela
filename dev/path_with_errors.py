import numpy as np

from dev.scenario.drone import create_drone_data
from dev.scenario.sensors import create_sensors_data
from dev.types.extended_position_data import ExtendedPositionData, NedData
from dev.utilities.noise import add_noise_to_polar_data
from dev.utilities.plots import show_figures
from dev.utilities.position import calc_polar_los, polar_to_ned

# scenario data
drone_data = create_drone_data()
sensors_data = create_sensors_data()

for sensor in sensors_data:
    los_sensor_polar = calc_polar_los(drone_data.ned, sensor)
    true_pos = ExtendedPositionData(ned=drone_data.ned, polar=los_sensor_polar)

    # noisy measurements:
    noisy_los_sensor_polar = add_noise_to_polar_data(los_sensor_polar)
    noisy_los_sensor_ned = polar_to_ned(noisy_los_sensor_polar)
    drone_coordinates = np.vstack([noisy_los_sensor_ned.x, noisy_los_sensor_ned.y, noisy_los_sensor_ned.z]).T
    temp = drone_coordinates + np.array([sensor.x, sensor.y, sensor.z])
    noisy_los_local_ned = NedData(t=drone_data.ned.t, x=temp[:, 0], y=temp[:, 1], z=temp[:, 2])
    plots = ExtendedPositionData(ned=noisy_los_local_ned, polar=noisy_los_sensor_polar)

    # plots:
    show_figures(true_pos, sensor, plots)
