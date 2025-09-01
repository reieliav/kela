from dataclasses import dataclass

from dev.types.drone_data import DroneData
from dev.types.extended_position_data import ExtendedPathData
from dev.types.sensor_data import SensorData


@dataclass
class PlotData:
    true: ExtendedPathData
    plots: ExtendedPathData
    sensor: SensorData


@dataclass
class DroneDetectionData:
    drone: DroneData
    detections: dict[str, PlotData]
