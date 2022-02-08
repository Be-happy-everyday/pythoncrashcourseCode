import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename =  'pythoncrashcourse_source\Chapter16_Code\JSON_FILES\data\eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

#readable_file = 'pythoncrashcourse_source\Chapter16_Code\JSON_FILES\data\\readable_eq_data.json'
#with open(readable_file, 'w') as f:
    #json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

mags, longs, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    longs.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#print(mags[:10])
#print(longs[:5])
#print(lats[:5])
# Map the earthquakes
data = [{
    'type' : 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [4*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes - 30 Days')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')