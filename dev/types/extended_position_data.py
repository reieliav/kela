from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import numpy as np


@dataclass
class GeoPointData:
    latitude: float
    longitude: float
    altitude: float


@dataclass
class GeoPathData:
    latitude: np.ndarray
    longitude: np.ndarray
    altitude: np.ndarray


@dataclass
class NedData:
    north: np.ndarray
    east: np.ndarray
    down: np.ndarray
    origin: Optional[GeoPointData] = None


@dataclass
class PolarData:
    r: np.ndarray
    az: np.ndarray
    el: np.ndarray
    origin: Optional[GeoPointData] = None


@dataclass
class ExtendedPathData:
    t: list[datetime]
    llh: GeoPathData
    ned: NedData
    polar: PolarData
