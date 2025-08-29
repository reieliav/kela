from dataclasses import dataclass


@dataclass
class SensorData:
    name: str
    x: float
    y: float
    z: float
