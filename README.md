# Kela - Drone Detections Dashboard
![Drone Detections Dashboard](/docs/dashboard.png)

An interactive dashboard for **drone detections**, combining 3D paths, time-series plots, and geospatial mapping.  
Built with [Plotly Dash](https://dash.plotly.com/) and [Folium](https://python-visualization.github.io/folium/).

---

## ✨ Features

- Interactive **3D drone path visualization**  
- **Time-series graphs** for latitude, longitude, and altitude  
- **True vs noisy trajectory** comparison  
- **Sensor fields of view** displayed on a Folium map  
- **Dark mode** interface  

---

## 🚀 Installation and run


```bash
## Clone the repository:
git clone https://github.com/reieliav/kela.git
cd kela
pip install -r requirements.txt


## run dashboard:
python.exe /dev/dash_server.py 


## run basic:
python.exe /dev/main.py 
```
![Drone Detections Dashboard](/docs/figs.png)
