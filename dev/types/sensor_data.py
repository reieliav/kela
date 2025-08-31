from dataclasses import dataclass

from dev.types.extended_position_data import GeoPointData
from enum import Enum, auto


class SensorType(Enum):
    RADAR = auto()
    # todo:
    # CAMERA = auto()
    # THERMAL = auto()
    # LIDAR = auto()


@dataclass
class SensorData:
    sensor_type: SensorType
    position: GeoPointData
    name: str
    plot_color: str
    rate: float
    mds: float  # (minimum detectable signal)
    az_noise_std: float  # degree
    el_noise_std: float  # degree
    rng_noise_std: float = None  # meters
    # todo: orientation, fov, resolution, 2d/3d, ..
