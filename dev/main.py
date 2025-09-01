from dev.scenario.drone import create_drone_data
from dev.scenario.sensors import create_sensors
from dev.types.plot_data import PlotData, DroneDetectionData
from dev.utilities.noise import add_noise_to_sensor_samples
from dev.utilities.figures.plots import create_sensor_figures, create_unified_figures
from dev.utilities.position import sample_path_in_sensor_frame

drones = create_drone_data()
sensors = create_sensors()

sensor_color_mapping = {s.name: s.plot_color for s in sensors}

scenario_data: dict[int, DroneDetectionData] = {}
for drone in drones:
    detections: dict[str, PlotData] = {}
    for sensor in sensors:
        true_pos = sample_path_in_sensor_frame(drone, sensor)
        plots = add_noise_to_sensor_samples(sensor, true_pos)
        sensor_data = PlotData(true=true_pos, plots=plots, sensor=sensor)
        detections[sensor.name] = sensor_data
        create_sensor_figures(sensor_data, show=True)

    create_unified_figures(DroneDetectionData(drone=drone, detections=detections), show=True)

# todo:
#  readme, requirements
