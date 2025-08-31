import math


def dbsm_to_m2(dbsm):
    return 10**(dbsm / 10)


def m2_to_dbsm(rcs_m2):
    return 10 * math.log10(rcs_m2)


def is_detected_by_radar(rcs_dbsm: float, distance_m: float, effective_mds: float):
    """
    Returns True if radar can detect a target with given RCS at a certain distance, according to sensor MDS.
    """
    return dbsm_to_m2(rcs_dbsm) >= effective_mds * distance_m ** 4
