from dataclasses import dataclass

from data_types.drone_data import DroneData
from data_types.extended_position_data import ExtendedPathData
from data_types.sensor_data import SensorData


@dataclass
class PlotData:
    true: ExtendedPathData
    plots: ExtendedPathData
    sensor: SensorData


@dataclass
class DroneDetectionData:
    drone: DroneData
    detections: dict[str, PlotData]
