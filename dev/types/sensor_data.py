from dataclasses import dataclass


@dataclass
class SensorData:
    name: str
    rate: float
    mds: float  # (minimum detectable signal)
    x: float
    y: float
    z: float
