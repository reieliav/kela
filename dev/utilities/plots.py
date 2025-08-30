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
        subplot_titles=("3D Path", "X over Path", "Y over Path", "Z over Path"),
        column_widths=[0.5, 0.5]  # give more space to 3D
    )

    # plot true (once):
    true_pos = sensors_data[0].true
    # 3D True + Noisy Path
    row = 1
    col = 1
    fig.add_trace(go.Scatter3d(x=true_pos.x, y=true_pos.y, z=true_pos.z, mode='lines+markers', name='True Path',
                               ), row=row, col=col)

    col = 2
    row = 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.x, mode="lines+markers", name="True X"), row=row, col=col)
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.y, mode="lines+markers", name="True Y"), row=row, col=col)
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.z, mode="lines+markers", name="True Z"), row=row, col=col)

    for sensor_data in sensors_data:
        sensor = sensor_data.sensor
        plots = sensor_data.plots

        # 3D True + Noisy Path
        row = 1
        col = 1
        fig.add_trace(go.Scatter3d(x=plots.x, y=plots.y, z=plots.z, mode='lines+markers', name=f'{sensor.name} Noisy Path',
                                   line=dict(dash='dash')), row=row, col=col)
        fig.add_trace(go.Scatter3d(x=[sensor.x], y=[sensor.y], z=[sensor.z], mode='markers',
                                   name=f'sensor position: {sensor.name}', showlegend=False,
                                   marker=dict(size=6)), row=row, col=col)

        # X
        row = 1
        col = 2
        fig.add_trace(go.Scatter(x=plots.t, y=plots.x, mode="lines+markers", name=f"{sensor.name} Noisy X"), row=row, col=col)

        # Y
        row += 1
        fig.add_trace(go.Scatter(x=plots.t, y=plots.y, mode="lines+markers", name=f"{sensor.name} Noisy Y"), row=row, col=col)

        # Z
        row += 1
        fig.add_trace(go.Scatter(x=plots.t, y=plots.z, mode="lines+markers", name=f"{sensor.name} Noisy Z"), row=row, col=col)

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
    # todo: plot as list of ExtendedPositionData

    true_pos = sensor_data.true
    sensor = sensor_data.sensor
    plots = sensor_data.plots

    fig = make_subplots(
        rows=6, cols=2,
        specs=[
            [{'type': 'scene', 'rowspan': 6}, {'type': 'xy'}],
            [None, {'type': 'xy'}],
            [None, {'type': 'xy'}],
            [None, {'type': 'xy'}],
            [None, {'type': 'xy'}],
            [None, {'type': 'xy'}],
        ],
        subplot_titles=("3D Path", "Azimuth",  "Elevation", "Range", "X over Path", "Y over Path", "Z over Path"),
        column_widths=[0.5, 0.5]  # give more space to 3D
    )

    # 3D True + Noisy Path
    row = 1
    col = 1
    fig.add_trace(go.Scatter3d(x=true_pos.x, y=true_pos.y, z=true_pos.z, mode='lines+markers', name='True Path',
                               line=dict(color='blue')), row=row, col=col)
    fig.add_trace(go.Scatter3d(x=plots.x, y=plots.y, z=plots.z, mode='lines+markers', name=f'{sensor.name} Noisy Path',
                               line=dict(color='orange', dash='dash')), row=row, col=col)
    fig.add_trace(go.Scatter3d(x=[sensor.x], y=[sensor.y], z=[sensor.z], mode='markers',
                               name=f'sensor position: {sensor.name}', showlegend=False,
                               marker=dict(size=6, color='red')), row=row, col=col)

    col = 2
    # Azimuth
    row = 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=np.degrees(true_pos.az), mode="lines+markers", name="Azimuth (°)"), row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=np.degrees(plots.az), mode="lines+markers", name="Azimuth noisy"), row=row, col=col)

    # Elevation
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=np.degrees(true_pos.el), mode="lines+markers", name="Elevation (°)"), row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=np.degrees(plots.el), mode="lines+markers", name="Elevation noisy"), row=row, col=col)

    # Range
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.r, mode="lines+markers", name="Range"), row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=plots.r, mode="lines+markers", name="Range noisy"), row=row, col=col)

    # X
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.x, mode="lines+markers", name="True X"), row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=plots.x, mode="lines+markers", name="Noisy X"), row=row, col=col)

    # Y
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.y, mode="lines+markers", name="True Y"), row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=plots.y, mode="lines+markers", name="Noisy Y"), row=row, col=col)

    # Z
    row += 1
    fig.add_trace(go.Scatter(x=true_pos.t, y=true_pos.z, mode="lines+markers", name="True Z"), row=row, col=col)
    fig.add_trace(go.Scatter(x=plots.t, y=plots.z, mode="lines+markers", name="Noisy Z"), row=row, col=col)

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
