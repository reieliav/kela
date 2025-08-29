import numpy as np

from dev.types.drone_data import DroneData
from dev.types.extended_position_data import NedData

# Generate a simple path
num_points = 50
drone_data = DroneData(
    ned=NedData(
        x=np.linspace(2000, 1000, num_points),
        y=np.linspace(10000, -1000, num_points),
        z=np.linspace(1000, 1200, num_points)),
    rcs_dbsm=10
)


def get_drone_data():
    return drone_data
