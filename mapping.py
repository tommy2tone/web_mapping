import folium
import pandas as pd

# Create initial map
volcano_map = folium.Map(location=[36.0710593, -78.5774039], zoom_start=4, tiles="OpenStreetMap")

# Create variable to store feature group attributes to add to map
feature_group = folium.FeatureGroup(name='Volcanoes')

# Variable to store volcano data
data = pd.read_csv('Volcanoes.csv')

# Variables to store volcano data to be used to create the markers
latitude = data['LAT']
longitude = data['LON']
elevation = data['ELEV']*3.28084
name = data['NAME']


# Function to determine marker color based on elevation
def marker_color(el):
    if el < 3000:
        return 'blue'
    elif 3000 <= el < 6000:
        return 'green'
    else:
        return 'red'


# For loop to generate markers from volcanoes csv file
for lat, lon, el, nam in zip(latitude, longitude, elevation, name):
    feature_group.add_child(folium.CircleMarker(location=[lat, lon],
                                                radius=10,
                                                popup=f'NAME: {nam} \n ELEV: {int(el)} ft',
                                                fill=True,
                                                color='',
                                                fill_color=marker_color(el),
                                                opacity=0
                                                ))


# Variable to store population data for each state
pop_data = pd.read_csv('pop_data.csv')

# Create choropleth features for population of each state and add to map
folium.Choropleth(geo_data=open('us-states.json', encoding='utf-8-sig').read(),
                  name='Population',
                  data=pop_data,
                  columns=['NAME', 'POPESTIMATE2018'],
                  key_on='feature.properties.name',
                  fill_color='YlGn',
                  fill_opacity=0.4,
                  line_opacity=0.5,
                  bins=5,
                  highlight=True,
                  legend_name='Population').add_to(volcano_map)


volcano_map.add_child(feature_group)

# Add layer control to turn on and off feature groups
folium.LayerControl().add_to(volcano_map)

volcano_map.save("Map.html")
