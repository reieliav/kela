import numpy as np

from dev.types.sensor_data import SensorData


def create_sensors_data() -> list[SensorData]:
    return [
        SensorData(name='Fox', rate=0.2, mds=0,
                   x=5000, y=10000, z=10000,
                   rng_noise_std=1000.0,
                   az_noise_std=np.radians(1.0),
                   el_noise_std=np.radians(0.5)
                   ),

        SensorData(name='Rabbit', rate=0.1, mds=0,
                   x=500, y=100, z=3000,
                   rng_noise_std=20.0,
                   az_noise_std=np.radians(4.0),
                   el_noise_std=np.radians(0.5)
                   )
    ]
