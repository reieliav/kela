from dev.types.sensor_data import SensorData


def create_sensors_data() -> list[SensorData]:
    return [
        SensorData(name='Fox', x=10000, y=10000, z=10000),
        SensorData(name='Rabbit', x=500, y=100, z=3000)
    ]
