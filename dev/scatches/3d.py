import numpy as np
import plotly.graph_objects as go

# Make a fake DEM with strong hills
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2)) * 50  # exaggerate heights

fig = go.Figure(go.Surface(z=Z, x=X, y=Y, colorscale="earth"))

# Adjust camera & aspect ratio to emphasize 3D
fig.update_layout(
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Height",
        aspectmode="manual",
        aspectratio=dict(x=1, y=1, z=0.5)  # squash horizontal, stretch vertical
    ),
    scene_camera=dict(eye=dict(x=2, y=2, z=1))  # tilt view
)

fig.show()
