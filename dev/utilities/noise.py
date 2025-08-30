import numpy as np

from dev.types.extended_position_data import PolarData, ExtendedPathData, NedData, GeoPathData
from dev.types.sensor_data import SensorData
from dev.utilities.position import polar_to_ned
import pymap3d as pm


def add_noise_to_sensor_samples(sensor: SensorData, los: ExtendedPathData):
    """
    The noise is added to the polar coordinates, which as these are the native sensor coordinates

    """
    num_points = len(los.polar.r)

    noisy_polar = PolarData(
        r=los.polar.r + np.random.normal(0, sensor.rng_noise_std, num_points),
        az=los.polar.az + np.random.normal(0, sensor.az_noise_std, num_points),
        el=los.polar.el + np.random.normal(0, sensor.el_noise_std, num_points),
        origin=sensor.position
    )

    noisy_ned = polar_to_ned(noisy_polar)
    origin = sensor.position
    latitude, longitude, altitude = pm.ned2geodetic(n=noisy_ned.north, e=noisy_ned.east, d=noisy_ned.down,
                                                    lat0=origin.latitude, lon0=origin.longitude, h0=origin.altitude)

    plots = ExtendedPathData(t=los.t, ned=noisy_ned, polar=noisy_polar,
                             llh=GeoPathData(latitude=latitude, longitude=longitude, altitude=altitude))

    return plots
