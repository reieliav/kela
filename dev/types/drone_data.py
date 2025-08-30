from dataclasses import dataclass
from datetime import datetime

from dev.types.extended_position_data import NedData


@dataclass
class DroneData:
    t: list[datetime]
    ned: NedData
    rcs_dbsm: float
