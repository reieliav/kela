import numpy as np

from dev.types.extended_position_data import GeoPointData
from dev.types.sensor_data import SensorData, SensorType


def create_sensors() -> list[SensorData]:
    return [
        SensorData(
            name='Fox',
            sensor_type=SensorType.RADAR,
            rate=1,
            mds=1e-12,  # Effective radar constant
            position=GeoPointData(latitude=32, longitude=35, altitude=0),
            rng_noise_std=0,
            az_noise_std=np.radians(0),
            el_noise_std=np.radians(0),
        ),

        SensorData(
            name='Rabbit',
            sensor_type=SensorType.RADAR,
            rate=0.1,
            mds=1e-15,  # Minimum detectable temperature difference [K]
            position=GeoPointData(latitude=32.01, longitude=35, altitude=0),
            rng_noise_std=300,
            az_noise_std=np.radians(.1),
            el_noise_std=np.radians(0.2)
        ),

        SensorData(
            name='Wolf',
            sensor_type=SensorType.RADAR,
            rate=0.1,
            mds=1e-15,  # Minimum detectable temperature difference [K]
            position=GeoPointData(latitude=32.02, longitude=35.02, altitude=76),
            rng_noise_std=300,
            az_noise_std=np.radians(.1),
            el_noise_std=np.radians(0.2)
        ),
    ]
