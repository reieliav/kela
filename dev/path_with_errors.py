import numpy as np
import matplotlib.pyplot as plt

# Generate a simple path
num_points = 50
x = np.linspace(0, 1000, num_points)
y = np.linspace(0, -1000, num_points)
z = np.linspace(0, 0, num_points)

# Sensor position
sensor_position = np.array([0, 0, 0])

# Vector from sensor to each drone position
points = np.vstack([x, y, z]).T
vectors = points - sensor_position  # shape (N, 3)

# Distances (range)
ranges = np.linalg.norm(vectors, axis=1)

# Azimuth (angle in XY plane)
azimuth = np.arctan2(vectors[:, 1], vectors[:, 0])

# Elevation (angle from XY plane upward)
elevation = np.arctan2(vectors[:, 2], np.linalg.norm(vectors[:, :2], axis=1))

# Convert to degrees
azimuth_deg = np.degrees(azimuth)
elevation_deg = np.degrees(elevation)

# Print first few for check
for i in range(5):
    print(f"Point {i}: Range={ranges[i]:.2f}, Az={azimuth_deg[i]:.2f}°, El={elevation_deg[i]:.2f}°")

# ---- PLOTS ----
fig = plt.figure(figsize=(14, 6))

# 3D Drone Path + Sensor
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot(x, y, z, marker='o', label="Drone Path")
ax1.scatter(*sensor_position, color='red', s=100, label="Sensor")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D Drone Path + Sensor')
ax1.legend()

# Plot x, y, z separately
ax2 = fig.add_subplot(132)
ax2.plot(range(num_points), x, label='X', marker='o')
ax2.plot(range(num_points), y, label='Y', marker='o')
ax2.plot(range(num_points), z, label='Z', marker='o')
ax2.set_xlabel('Point Index')
ax2.set_ylabel('Coordinate Value')
ax2.set_title('Coordinates over Path')
ax2.legend()

# Plot Azimuth & Elevation
ax3 = fig.add_subplot(133)
ax3.plot(range(num_points), azimuth_deg, label='Azimuth (°)', marker='o')
ax3.plot(range(num_points), elevation_deg, label='Elevation (°)', marker='o')
ax3.set_xlabel('Point Index')
ax3.set_ylabel('Angle (degrees)')
ax3.set_title('Sensor View Angles')
ax3.legend()

plt.tight_layout()
plt.show()
