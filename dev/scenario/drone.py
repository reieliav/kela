from datetime import datetime, timedelta

import numpy as np

from dev.types.drone_data import DroneData
from dev.types.extended_position_data import GeoPathData


def create_drone_data():
    # Generate a simple path
    num_points = 50
    time_start = datetime(year=2025, month=8, day=29, hour=14, minute=23, second=23)
    delta_time = timedelta(seconds=7)

    drone_data = DroneData(
        t=[time_start + i * delta_time for i in range(num_points)],
        lla=GeoPathData(
            latitude=np.linspace(31.9, 32, num_points),
            longitude=np.linspace(34.9, 35, num_points),
            altitude=np.linspace(2000, 1000, num_points),
        ),
        rcs_dbsm=10
    )
    return drone_data
