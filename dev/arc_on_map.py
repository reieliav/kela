import folium
import numpy as np

# Drone parameters
drone_lat, drone_lon = 32.0853, 34.7818
heading, fov, radius_m = 45, 90, 200

# Generate arc points with random noise in distance
angles = np.linspace(heading - fov/2, heading + fov/2, 60)
points = []
for ang in angles:
    # Add random noise +/- 20% of radius
    noisy_radius = radius_m * np.random.uniform(0.8, 1.2)
    # Convert bearing + distance to lat/lon
    R = 6378137
    dlat = (noisy_radius * np.cos(np.deg2rad(ang))) / R
    dlon = (noisy_radius * np.sin(np.deg2rad(ang))) / (R * np.cos(np.deg2rad(drone_lat)))
    points.append((drone_lat + np.rad2deg(dlat), drone_lon + np.rad2deg(dlon)))

# Build FOV polygon
fov_polygon = [(drone_lat, drone_lon)] + points + [(drone_lat, drone_lon)]

# --- Folium map ---
m = folium.Map(location=[drone_lat, drone_lon], zoom_start=17)

# Drone marker
folium.Marker([drone_lat, drone_lon], tooltip="Drone").add_to(m)

# FOV polygon
folium.Polygon(locations=fov_polygon, color="cyan", fill=True, fill_color="cyan",
               fill_opacity=0.3, tooltip="Sensor FOV (noisy)").add_to(m)

m.save("drone_fov_noisy.html")
