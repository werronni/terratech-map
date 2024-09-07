import folium
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv("restos.txt")
rest = data['rest']
lat = data['lat']
lon = data['lon']
fert = data['fert']
addr = data['addr']
phone = data['phone']


def color_change(fert):
    if (fert < 5):
        return ('green')
    elif (5 <= fert < 15):
        return ('orange')
    else:
        return ('red')


map = folium.Map(location=[51.1801, 71.446], zoom_start=12)

marker_cluster = MarkerCluster().add_to(map)

for rest, lat, lon, fert, addr, phone in zip(rest, lat, lon, fert, addr, phone):
    folium.Marker(location=[lat, lon], popup=str(rest) + "\nУдобрение: " + str(fert) + " кг\nАдрес: "+ addr + "\nТелефон: "+ phone,
                  icon=folium.Icon(color=color_change(fert))).add_to(marker_cluster)

map.save("map1.html")
