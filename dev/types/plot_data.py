from dataclasses import dataclass

from dev.types.extended_position_data import ExtendedPositionData
from dev.types.sensor_data import SensorData


@dataclass
class PlotData:
    true: ExtendedPositionData
    plots: ExtendedPositionData
    sensor: SensorData
