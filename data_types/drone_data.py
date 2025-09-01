from dataclasses import dataclass
from datetime import datetime

from data_types.extended_position_data import GeoPathData


@dataclass
class DroneData:
    id: int
    t: list[datetime]
    llh: GeoPathData
    rcs_dbsm: float
    # todo 1: spectral heat signature, max speed, curves spec, climbing speed, ...,
    # todo 2: simple kinematic engine, path generator, fleet, ground tracking (control height agl).
    # todo 3: visual characters, acoustic characters (for acoustic sensors), reflectivity, brightness..
