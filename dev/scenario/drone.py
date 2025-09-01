from datetime import datetime, timedelta

import numpy as np

from dev.types.drone_data import DroneData
from dev.types.extended_position_data import GeoPathData


# todo: add drone_type
def create_drone_data() -> list[DroneData]:
    # Generate a simple path
    num_points = 50
    time_start = datetime(year=2025, month=8, day=29, hour=14, minute=23, second=23)
    delta_time = timedelta(seconds=7)

    return [
        DroneData(
            id=1,
            t=[time_start + i * delta_time for i in range(num_points)],
            rcs_dbsm=-20,
            llh=GeoPathData(
                latitude=np.linspace(32.3, 32.4, num_points),
                longitude=np.linspace(36., 34.8, num_points),
                altitude=np.linspace(100, 100, num_points),
            ),
        ),

        DroneData(
            id=2,
            t=[time_start + i * delta_time for i in range(num_points)],
            rcs_dbsm=-10,
            llh=GeoPathData(
                latitude=np.linspace(32., 32.14, num_points),
                longitude=np.linspace(36, 34.5, num_points),
                altitude=np.linspace(100, 100, num_points),
            ),
        )
    ]
