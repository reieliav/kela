import numpy as np

from dev.types.extended_position_data import GeoPointData
from dev.types.sensor_data import SensorData


def create_sensors() -> list[SensorData]:
    return [
        SensorData(name='Fox', rate=1, mds=0,
                   position=GeoPointData(latitude=32, longitude=34, altitude=0),
                   rng_noise_std=0,
                   az_noise_std=np.radians(0),
                   el_noise_std=np.radians(0)
                   ),

        SensorData(name='Rabbit', rate=0.1, mds=0,
                   position=GeoPointData(latitude=32.1, longitude=34.7, altitude=0),
                   rng_noise_std=1000.0,
                   az_noise_std=np.radians(.1),
                   el_noise_std=np.radians(0.2)
                   ),
    ]
