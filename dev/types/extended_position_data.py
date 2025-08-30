from dataclasses import dataclass
from datetime import datetime

import numpy as np


@dataclass
class NedData:
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray


@dataclass
class PolarData:
    r: np.ndarray
    az: np.ndarray
    el: np.ndarray


@dataclass
class ExtendedPathData(NedData, PolarData):
    t: list[datetime]

    @classmethod
    def from_parts(cls, ned: NedData, polar: PolarData, t: list[datetime]):
        return cls(
            t=t,
            x=ned.x,
            y=ned.y,
            z=ned.z,
            r=polar.r,
            az=polar.az,
            el=polar.el
        )
