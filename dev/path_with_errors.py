
from dev.scenario.drone import create_drone_data
from dev.scenario.sensors import create_sensors_data
from dev.utilities.noise import add_noise_to_sensor_samples
from dev.utilities.plots import show_figures
from dev.utilities.position import sample_path_in_sensor_frame

# scenario data
drone_data = create_drone_data()
sensors_data = create_sensors_data()

for sensor in sensors_data:
    true_pos = sample_path_in_sensor_frame(drone_data.ned, sensor)
    plots = add_noise_to_sensor_samples(sensor, true_pos)
    show_figures(true_pos, sensor, plots)
