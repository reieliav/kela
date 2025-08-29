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

    @classmethod
    def from_parts(cls, ned: NedData, polar: PolarData):
        return cls(
            t=ned.t,
            x=ned.x,
            y=ned.y,
            z=ned.z,
            r=polar.r,
            az=polar.az,
            el=polar.el
        )
