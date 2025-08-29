import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dev.types.extended_position_data import ExtendedPositionData


def show_figures(true_pos: ExtendedPositionData, plots: ExtendedPositionData):
    # todo: plot as list of ExtendedPositionData
    fig = make_subplots(
        rows=6, cols=2,
        specs=[
            [{'type': 'xy'}, {'type': 'scene', 'rowspan': 6}],
            [{'type': 'xy'}, None],
            [{'type': 'xy'}, None],
            [{'type': 'xy'}, None],
            [{'type': 'xy'}, None],
            [{'type': 'xy'}, None],
        ],
        subplot_titles=("Azimuth", "3D Path", "Elevation", "Range", "X over Path", "Y over Path", "Z over Path"),
        column_widths=[0.5, 0.5]  # give more space to 3D
    )

    # 3D True + Noisy Path
    row = 1
    fig.add_trace(go.Scatter3d(x=true_pos.x, y=true_pos.y, z=true_pos.z, mode='lines+markers', name='True Path',
                               line=dict(color='blue')), row=row, col=2)
    fig.add_trace(go.Scatter3d(x=plots.x, y=plots.y, z=plots.z, mode='lines+markers', name='Noisy Path',
                               line=dict(color='orange', dash='dash')), row=row, col=2)
    fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers', name='Sensor',
                               marker=dict(size=6, color='red')), row=row, col=2)

    # Azimuth
    row = 1
    fig.add_trace(go.Scatter(y=np.degrees(true_pos.az), mode="lines+markers", name="Azimuth (°)"), row=row, col=1)
    fig.add_trace(go.Scatter(y=np.degrees(plots.az), mode="lines+markers", name="Azimuth noisy"), row=row, col=1)

    # Elevation
    row += 1
    fig.add_trace(go.Scatter(y=np.degrees(true_pos.el), mode="lines+markers", name="Elevation (°)"), row=row, col=1)
    fig.add_trace(go.Scatter(y=np.degrees(plots.el), mode="lines+markers", name="Elevation noisy"), row=row, col=1)

    # Range
    row += 1
    fig.add_trace(go.Scatter(y=true_pos.r, mode="lines+markers", name="Range"), row=row, col=1)
    fig.add_trace(go.Scatter(y=plots.r, mode="lines+markers", name="Range noisy"), row=row, col=1)

    # X
    row += 1
    fig.add_trace(go.Scatter(y=true_pos.x, mode="lines+markers", name="True X"), row=row, col=1)
    fig.add_trace(go.Scatter(y=plots.x, mode="lines+markers", name="Noisy X"), row=row, col=1)

    # Y
    row += 1
    fig.add_trace(go.Scatter(y=true_pos.y, mode="lines+markers", name="True Y"), row=row, col=1)
    fig.add_trace(go.Scatter(y=plots.y, mode="lines+markers", name="Noisy Y"), row=row, col=1)

    # Z
    row += 1
    fig.add_trace(go.Scatter(y=true_pos.z, mode="lines+markers", name="True Z"), row=row, col=1)
    fig.add_trace(go.Scatter(y=plots.z, mode="lines+markers", name="Noisy Z"), row=row, col=1)

    # Layout tweaks
    fig.update_layout(height=900, width=1200, title_text="Drone Path & Radar Measurements", showlegend=True)

    fig.show()
