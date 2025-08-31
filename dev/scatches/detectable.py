# too simplified

# ------------------- RADAR -------------------
MDS_radar_eff = 3.2e-11  # Effective radar constant


def is_detected_by_radar(rcs_m2, distance_m, effective_mds=MDS_radar_eff):
    """Check if a target is detectable by radar."""
    return rcs_m2 >= effective_mds * distance_m ** 4


# ------------------- THERMAL (IR) -------------------
NETD = 0.05  # Minimum detectable temperature difference [K]


def is_detected_by_thermal(delta_T, netd=NETD):
    """Check if a target is detectable by thermal sensor."""
    return delta_T >= netd


# ------------------- LIDAR -------------------
MDS_lidar_eff = 1e-10  # Effective LiDAR constant (folds in power, aperture, efficiency)


def is_detected_by_lidar(reflectivity, distance_m, effective_mds=MDS_lidar_eff):
    """Check if a target is detectable by LiDAR."""
    return reflectivity >= effective_mds * distance_m ** 4


# ------------------- CAMERA -------------------
MDS_camera_eff = 5e-5  # Effective brightness constant


def is_detected_by_camera(brightness, distance_m, effective_mds=MDS_camera_eff):
    """Check if a target is detectable by camera."""
    return brightness >= effective_mds * distance_m ** 2


# ------------------- EXAMPLES -------------------
rcs = 0.05
delta_T = 0.06
reflectivity = 0.1
brightness = 0.01
distance = 1000

print("Radar detected:", is_detected_by_radar(rcs, distance))
print("Thermal detected:", is_detected_by_thermal(delta_T))
print("LiDAR detected:", is_detected_by_lidar(reflectivity, distance))
print("Camera detected:", is_detected_by_camera(brightness, distance))