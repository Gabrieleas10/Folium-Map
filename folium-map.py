import folium
import pandas as pd
from folium.plugins import HeatMap ,MarkerCluster , MiniMap
from tqdm import tqdm

df = pd.read_excel('GIT_Folium.xlsx')

mapa = folium.Map(location = [-5.084678, -39.483764] ,
                  tiles = 'OpenStreetMap',
                  zoom_start = 7)

mc = MarkerCluster()

tqdm.pandas()
for i in tqdm(range(0 , len(df['LAT']))):
  x = df['LAT'][i]
  y = df['LON'][i]
  info = str(df['Costumers'][i])
  mc.add_child(folium.Marker(location = (x,y) ,
                               popup = 'Costumers: '+str(info),
                               draggable = True,
                               tooltip = 'Latitude: '+str(x)+' ; '+'Longitude: '+str(y),
                               icon = folium.Icon(color='orange',icon='home')))

mapa.add_child(folium.LatLngPopup())

mapa.add_child(mc)

mapa.save('GDMap.html')