from dataclasses import dataclass

from dev.types.extended_position_data import ExtendedPathData
from dev.types.sensor_data import SensorData


@dataclass
class PlotData:
    true: ExtendedPathData
    plots: ExtendedPathData
    sensor: SensorData
