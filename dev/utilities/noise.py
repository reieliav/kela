import numpy as np

from dev.types.extended_position_data import PolarData


def add_noise_to_polar_data(los: PolarData):
    num_points = len(los.r)

    # todo: this is sensor spec..
    rng_noise_std = 20.0  # meters
    az_noise_std = np.radians(1.0)  # ~1 degree
    el_noise_std = np.radians(0.5)  # ~0.5 degree

    return PolarData(
        r=los.r + np.random.normal(0, rng_noise_std, num_points),
        az=los.az + np.random.normal(0, az_noise_std, num_points),
        el=los.el + np.random.normal(0, el_noise_std, num_points))
