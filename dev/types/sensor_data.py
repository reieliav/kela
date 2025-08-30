from dataclasses import dataclass

from dev.types.extended_position_data import GeoPointData


@dataclass
class SensorData:
    position: GeoPointData
    name: str
    rate: float
    mds: float  # (minimum detectable signal)
    rng_noise_std: float  # meters
    az_noise_std: float  # degree
    el_noise_std: float  # degree
    # todo: orientation, fov, resolution, mds, 2d/3d, ..
