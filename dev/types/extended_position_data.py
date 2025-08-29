from dataclasses import dataclass
from datetime import datetime

import numpy as np


@dataclass
class NedData:
    t: list[datetime]
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray


@dataclass
class PolarData:
    t: list[datetime]
    r: np.ndarray
    az: np.ndarray
    el: np.ndarray


@dataclass
class ExtendedPositionData(NedData, PolarData):
    def __init__(self, ned: NedData, polar: PolarData):
        self.t = ned.t
        self.x = ned.x
        self.y = ned.y
        self.z = ned.z
        self.r = polar.r
        self.az = polar.az
        self.el = polar.el

