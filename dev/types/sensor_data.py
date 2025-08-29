from dataclasses import dataclass


@dataclass
class SensorData:
    name: str
    rate: float
    mds: float  # (minimum detectable signal)
    x: float
    y: float
    z: float
    rng_noise_std: float  # meters
    az_noise_std: float  # degree
    el_noise_std: float  # degree
