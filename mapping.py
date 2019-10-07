import folium
import pandas as pd

map = folium.Map(location=[36.0710593, -78.5774039], zoom_start=4, tiles="OpenStreetMap")

feature_group = folium.FeatureGroup()
data = pd.read_csv('Volcanoes.csv')
latitude = data['LAT']
longitude = data['LON']

for lat, lon in zip(latitude, longitude):
    feature_group.add_child(folium.Marker(location=[lat, lon], popup='Hi I am a marker', icon=folium.Icon(color='green')))

feature_group.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))


map.add_child(feature_group)
map.save("Map.html")
