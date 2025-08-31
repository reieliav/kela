
from dev.scenario.drone import create_drone_data
from dev.scenario.sensors import create_sensors
from dev.types.plot_data import PlotData
from dev.utilities.noise import add_noise_to_sensor_samples
from dev.utilities.figures.plots import create_sensor_figures, create_unified_figures
from dev.utilities.position import sample_path_in_sensor_frame

drone_data = create_drone_data()
sensors = create_sensors()

sensors_data = []
for sensor in sensors:
    true_pos = sample_path_in_sensor_frame(drone_data, sensor)
    plots = add_noise_to_sensor_samples(sensor, true_pos)
    sensor_data = PlotData(true=true_pos, plots=plots, sensor=sensor)
    create_sensor_figures(sensor_data, show=True)
    sensors_data.append(sensor_data)

create_unified_figures(sensors_data, show=True)

# todo:
#  map, dash.
#  readme, requirements
