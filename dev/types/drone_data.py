from dataclasses import dataclass
from datetime import datetime

from dev.types.extended_position_data import GeoPathData


@dataclass
class DroneData:
    t: list[datetime]
    lla: GeoPathData
    rcs_dbsm: float
    # todo 1: spectral heat signature, max speed, curves spec, climbing speed, ...,
    # todo 2: path generator, fleet, ground tracking (control height agl).
    # todo 3: visual characters, acoustic characters (for acoustic sensors), reflectivity, brightness..

