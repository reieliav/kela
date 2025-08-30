import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dev.types.plot_data import PlotData


def show_unified_figures(sensors_data: list[PlotData]):
    fig = make_subplots(
        rows=3, cols=2,
        specs=[
            [{'type': 'scene', 'rowspan': 3}, {'type': 'xy'}],
            [None, {'type': 'xy'}],
            [None, {'type': 'xy'}],

        ],
        subplot_titles=("3D Path (LLH)", "Latitude", "Longitude", "Altitude"),
        column_widths=[0.5, 0.5]  # give more space to 3D
    )

    # plot true (once):
    true_pos = sensors_data[0].true
    # 3D True + Noisy Path
    row = 1
    col = 1
    fig.add_trace(go.Scatter3d(x=true_pos.llh.latitude, y=true_pos.llh.longitude, z=true_pos.llh.altitude,
                               mode='lines+markers', name='True Path (LLH)'),
                  row=row, col=col)

    col = 2
    row = 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.llh.latitude, mode="lines+markers", name="True latitude"),
                  row=row, col=col)
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.llh.longitude, mode="lines+markers", name="True longitude"),
                  row=row, col=col)
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.llh.altitude, mode="lines+markers", name="True altitude"),
                  row=row, col=col)

    for sensor_data in sensors_data:
        sensor = sensor_data.sensor
        plots = sensor_data.plots

        # 3D True + Noisy Path
        row = 1
        col = 1
        fig.add_trace(go.Scatter3d(x=plots.llh.latitude, y=plots.llh.longitude, z=plots.llh.altitude,
                                   mode='lines+markers', name=f'{sensor.name} Noisy Path', line=dict(dash='dash')),
                      row=row, col=col)
        origin = sensor.position
        fig.add_trace(go.Scatter3d(x=[origin.latitude], y=[origin.longitude], z=[origin.altitude], mode='markers',
                                   name=f'{sensor.name} pos.', showlegend=False, marker=dict(size=6)),
                      row=row, col=col)

        # X
        row = 1
        col = 2
        fig.add_trace(go.Scatter(x=plots.t, y=plots.llh.latitude, mode="lines+markers",
                                 name=f"{sensor.name} Noisy latitude"),
                      row=row, col=col)

        # Y
        row += 1
        fig.add_trace(go.Scatter(x=plots.t, y=plots.llh.longitude, mode="lines+markers",
                                 name=f"{sensor.name} Noisy longitude"),
                      row=row, col=col)

        # Z
        row += 1
        fig.add_trace(go.Scatter(x=plots.t, y=plots.llh.altitude, mode="lines+markers",
                                 name=f"{sensor.name} Noisy altitude"),
                      row=row, col=col)

        # Layout tweaks
        fig.update_layout(
            title={
                "text": "<b>Sensors Measurements for Drone Path</b>",
                "y": 0.95,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            title_font=dict(size=24),
            showlegend=True, template="plotly_dark")

    fig.show()


def show_sensor_figures(sensor_data: PlotData):
    # todo: plot as list of ExtendedPathData

    true_pos = sensor_data.true
    sensor = sensor_data.sensor
    plots = sensor_data.plots

    fig = make_subplots(
        rows=6, cols=2,
        specs=[
            [{'type': 'scene', 'rowspan': 3}, {'type': 'xy'}],
            [None, {'type': 'xy'}],
            [None, {'type': 'xy'}],
            [{'type': 'scene', 'rowspan': 3}, {'type': 'xy'}],
            [None, {'type': 'xy'}],
            [None, {'type': 'xy'}],
        ],
        subplot_titles=("3D Path (NED)", "Azimuth",  "Elevation", "Range",
                        "3D Path (LLH)", "X over Path", "Y over Path", "Z over Path"),
        column_widths=[0.5, 0.5]  # give more space to 3D
    )

    # 3D True + Noisy Path
    col = 1
    row = 1
    fig.add_trace(go.Scatter3d(x=true_pos.ned.north, y=true_pos.ned.east, z=-true_pos.ned.down, name='True Path (NED)',
                               mode='lines+markers', line=dict(color='blue')),
                  row=row, col=col)
    fig.add_trace(go.Scatter3d(x=plots.ned.north, y=plots.ned.east, z=-plots.ned.down, mode='lines+markers',
                               name=f'{sensor.name} Noisy Path', line=dict(color='orange', dash='dash')),
                  row=row, col=col)
    fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers', name=f'sensor position: {sensor.name}',
                               showlegend=False, marker=dict(size=6)),
                  row=row, col=col)

    row = 4
    fig.add_trace(go.Scatter3d(x=true_pos.llh.latitude, y=true_pos.llh.longitude, z=true_pos.llh.altitude,
                               mode='lines+markers', name='True Path (Geo)', line=dict(color='blue')),
                  row=row, col=col)
    fig.add_trace(go.Scatter3d(x=plots.llh.latitude, y=plots.llh.longitude, z=plots.llh.altitude, mode='lines+markers',
                               name=f'{sensor.name} Noisy Path', line=dict(color='orange', dash='dash')),
                  row=row, col=col)
    origin = sensor.position
    fig.add_trace(go.Scatter3d(x=[origin.latitude], y=[origin.longitude], z=[origin.altitude], showlegend=False,
                               mode='markers', name=f'sensor position: {sensor.name}', marker=dict(size=6)),
                  row=row, col=col)

    col = 2
    # Azimuth
    row = 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=np.degrees(true_pos.polar.az), mode="lines+markers", name="Azimuth (°)"),
                  row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=np.degrees(plots.polar.az), mode="lines+markers", name="Azimuth noisy"),
                  row=row, col=col)

    # Elevation
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=np.degrees(true_pos.polar.el), mode="lines+markers", name="Elevation (°)"),
                  row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=np.degrees(plots.polar.el), mode="lines+markers", name="Elevation noisy"),
                  row=row, col=col)

    # Range
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.polar.r, mode="lines+markers", name="Range"),
                  row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=plots.polar.r, mode="lines+markers", name="Range noisy"),
                  row=row, col=col)

    # X
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.ned.north, mode="lines+markers", name="True north"),
                  row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=plots.ned.north, mode="lines+markers", name="Noisy north"),
                  row=row, col=col)

    # Y
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.ned.east, mode="lines+markers", name="True east"),
                  row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=plots.ned.east, mode="lines+markers", name="Noisy east"),
                  row=row, col=col)

    # Z
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=-true_pos.ned.down, mode="lines+markers", name="True altitude"),
                  row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=-plots.ned.down, mode="lines+markers", name="Noisy altitude"),
                  row=row, col=col)

    # Layout tweaks
    fig.update_layout(
        title={
            "text": f"<b>{sensor.name} sensor measurements for drone path</b>",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top"
        },
        title_font=dict(size=24), showlegend=True, template="plotly_dark",
    )

    fig.show()
