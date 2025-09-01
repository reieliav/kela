import numpy as np

from data_types.extended_position_data import GeoPointData
from data_types.sensor_data import SensorData, SensorType


def create_sensors() -> list[SensorData]:
    return [
        SensorData(
            name='Fox',
            sensor_type=SensorType.RADAR,
            rate=1,
            mds=1e-19,  # Effective radar constant
            position=GeoPointData(latitude=32.26, longitude=35.4, altitude=0),
            rng_noise_std=0,
            az_noise_std=np.radians(0),
            el_noise_std=np.radians(0),
            plot_color='green',
            heading=30,
            fov=30
        ),

        SensorData(
            name='Rabbit',
            sensor_type=SensorType.RADAR,
            rate=1,
            mds=1e-20,  # Minimum detectable temperature difference [K]
            position=GeoPointData(latitude=32.08, longitude=35.509, altitude=0),
            rng_noise_std=300,
            az_noise_std=np.radians(.1),
            el_noise_std=np.radians(0.2),
            plot_color='cyan',
            heading=90,
            fov=70
        ),

        SensorData(
            name='Wolf',
            sensor_type=SensorType.RADAR,
            rate=0.1,
            mds=1e-18,  # Minimum detectable temperature difference [K]
            position=GeoPointData(latitude=32.02, longitude=35.02, altitude=76),
            rng_noise_std=300,
            az_noise_std=np.radians(.1),
            el_noise_std=np.radians(0.2),
            plot_color='orange',
            heading=150,
            fov=60
        ),
    ]
