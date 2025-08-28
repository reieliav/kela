import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objects as go

from dev.drone import path



df = pd.DataFrame(path, columns=["lat", "lon", "height", "time"])
df["time"] = pd.to_datetime(df["time"])

map_fig = go.Figure(go.Scattermap(
    lat=df["lat"],
    lon=df["lon"],
    mode="markers+lines",
    marker=dict(size=8, color=df["height"], colorscale="Viridis", showscale=True),
    text=[f"Time: {t}, Height: {h}m" for t, h in zip(df["time"], df["height"])]
))

map_fig.update_layout(
    map=dict(
        style="open-street-map",  # works with MapLibre
        center=dict(lat=df["lat"].mean(), lon=df["lon"].mean()),
        zoom=8
    ),
    margin={"r":0,"t":0,"l":0,"b":0},
    height=500
)

# Altitude vs Time figure
alt_fig = go.Figure(go.Scatter(
    x=df["time"], y=df["height"], mode="lines+markers"
))
alt_fig.update_layout(
    title="Drone Altitude Over Time",
    xaxis_title="Time",
    yaxis_title="Height (m)",
    height=300
)

# Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H2("Drone Path Dashboard"),
    dcc.Graph(figure=map_fig),
    dcc.Graph(figure=alt_fig)
])

if __name__ == "__main__":
    app.run(debug=True)
