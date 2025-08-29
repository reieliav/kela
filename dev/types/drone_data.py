from dataclasses import dataclass

from dev.types.extended_position_data import NedData


@dataclass
class DroneData:
    ned: NedData
    rcs_dbsm: float
