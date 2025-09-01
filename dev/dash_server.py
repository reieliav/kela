import dash
import dash_bootstrap_components as dbc
import folium
from dash import html, dcc
from dash.dependencies import Input, Output
from folium.plugins import AntPath, Fullscreen, MousePosition

from dev.scenario.drone import create_drone_data
from dev.scenario.sensors import create_sensors
from dev.types.plot_data import DroneDetectionData, PlotData
from dev.utilities.detection_threshold import dbsm_to_m2
from dev.utilities.figures.dash_plots import create_dash_sensor_figures, create_dash_unified_figures
from dev.utilities.noise import add_noise_to_sensor_samples
from dev.utilities.position import sample_path_in_sensor_frame
import requests

drones = create_drone_data()
sensors = create_sensors()

sensor_color_mapping = {s.name: s.plot_color for s in sensors}


def get_available_tiles():
    # todo: move to utils/map
    tile_url = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/0/0/0"
    try:
        r = requests.get(tile_url, timeout=2)
        if r.status_code == 200:
            return "Esri.WorldImagery"
    except requests.RequestException:
        pass
    return "OpenStreetMap"


tiles = get_available_tiles()
scenario_data: dict[int, DroneDetectionData] = {}
for drone in drones:
    detections: dict[str, PlotData] = {}
    for sensor in sensors:
        true_pos = sample_path_in_sensor_frame(drone, sensor)
        plots = add_noise_to_sensor_samples(sensor, true_pos)
        detections[sensor.name] = PlotData(true=true_pos, plots=plots, sensor=sensor)

    scenario_data[drone.id] = DroneDetectionData(drone=drone, detections=detections)


def create_map(drone_value, sensor_value):
    # todo: move to utils/map
    drone_rcs = 1
    m = folium.Map(location=[31.8, 35.2], zoom_start=8, tiles=tiles)
    Fullscreen(position="topright", force_separate_button=True).add_to(m)
    MousePosition(separator=" , ", num_digits=6, prefix="Coordinates:").add_to(m)
    for drone_data in drones:
        html_content = f"""
<h4>Drone id: {drone_data.id}</h4>
<p>RCS: {drone_data.rcs_dbsm} [dBsm]</p>
        """
        iframe = folium.IFrame(html=html_content, width='150', height='100')
        drone_popup = folium.Popup(iframe, max_width=250)
        if str(drone_data.id) == drone_value.split(' ')[1]:
            AntPath(locations=[(lat, lon) for lat, lon in zip(drone_data.llh.latitude, drone_data.llh.longitude)],
                    weight=7, delay=1000, dash_array=[10, 20], color='red', popup=drone_popup).add_to(m)
            for sensor_name, sensor_detections in scenario_data[drone_data.id].detections.items():
                radius = 40 if sensor_name == sensor_value else 20
                plots_data = sensor_detections.plots.llh
                for i in range(len(plots_data.latitude)):
                    folium.Circle((plots_data.latitude[i], plots_data.longitude[i]),
                                        color=sensor_color_mapping[sensor_name], fill=True,
                                        popup=f'plot #{i} ({sensor_name})', radius=radius).add_to(m)
            drone_rcs = dbsm_to_m2(drone_data.rcs_dbsm)

        else:
            folium.PolyLine(
                locations=[(lat, lon) for lat, lon in zip(drone_data.llh.latitude, drone_data.llh.longitude)],
                weight=5, delay=1000, color='gray',  popup=drone_popup).add_to(m)

    for s in sensors:
        html_content = f"""
<h4>{s.name} ({s.sensor_type.name.lower()})</h4>
<p>LLH: ({s.position.latitude}, {s.position.longitude}, {s.position.altitude})</p>
<p>mds: {s.mds}</p>
<p>heading: {s.heading}</p>
<p>fov: {s.fov}</p>
"""
        iframe = folium.IFrame(html=html_content, width='200', height='200')
        popup = folium.Popup(iframe, max_width=250)
        folium.Marker([s.position.latitude, s.position.longitude], popup=popup).add_to(m)
        folium.plugins.SemiCircle(
            (s.position.latitude, s.position.longitude),
            radius=50*drone_rcs/(s.mds**0.25),
            direction=s.heading,
            arc=s.fov,
            color='red',
            fill_color=s.plot_color,
            opacity=0.5,
        ).add_to(m)

    return m.get_root().render()


# Initialize Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
fig_3d_init, fig_profiles_init = create_dash_sensor_figures(scenario_data[drones[0].id].detections[sensors[0].name])
app.layout = dbc.Container([
    html.H2('Drone Detections - Path and plots',  style={'textAlign': 'center'}),
    html.H5('Choose drone and sensor:'),
    dbc.Row([
        dcc.Dropdown(
            id="drone_value",
            options=[{"label": f'Drone {s.id}', "value": f'Drone {s.id}'} for s in drones],
            value=f'Drone {drones[0].id}',
            clearable=False,
            style={"width": "150px", 'color': 'black'}),
        dcc.Dropdown(
            id="sensor_value",
            options=([{"label": s.name, "value": s.name} for s in sensors] +
                     [{"label": 'all sensors', "value": 'all sensors'}]),
            value=sensors[0].name,
            clearable=False,
            style={"width": "150px", 'color': 'black'}),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='plot1', figure=fig_3d_init,
                          style={'width': '100%', 'height': '100%', 'border': 'none'}), width=3),
        dbc.Col(dcc.Graph(id='plot2', figure=fig_profiles_init,
                          style={'width': '100%', 'height': '100%', 'border': 'none'}), width=4),
        dbc.Col(html.Iframe(id='map-frame', srcDoc=create_map('Drone 1', 'all sensors'),
                            style={'width': '100%', 'height': '100%', 'border': 'none'}), width=5),
    ],  style={'height': '800px'})  # g-2 adds spacing between columns
], fluid=True, style={'background-color': '#111', 'color': 'white', 'padding': '10px'})


# Callback to update all frames
@app.callback(
    Output('plot1', 'figure'),
    Output('plot2', 'figure'),
    Output('map-frame', 'srcDoc'),
    Input('sensor_value', 'value'),
    Input('drone_value', 'value')
)
def update_all(sensor_value, drone_value):
    map_html = create_map(drone_value, sensor_value)
    drone_id = int(drone_value.split(' ')[1])

    if sensor_value == 'all sensors':
        fig_3d, fig_profiles = create_dash_unified_figures(scenario_data[drone_id])
    else:
        fig_3d, fig_profiles = create_dash_sensor_figures(scenario_data[drone_id].detections[sensor_value])

    return fig_3d, fig_profiles, map_html


if __name__ == '__main__':
    app.run(dev_tools_hot_reload=False)
