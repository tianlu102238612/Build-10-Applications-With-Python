#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 00:22:21 2020

@author: tianlu
"""


import folium
import pandas

map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcannoes")

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def iconColor(el):
    if el<1000:
        return 'green'
    elif 1000<=el<3000:
        return 'orange'
    else:
        return 'red'

for lt,ln,nm,el in zip(lat,lon,name,elev):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=str(nm)+" "+str(el),icon=folium.Icon(color=iconColor(el))))

fgp = folium.FeatureGroup(name="Population")
geoData = open('world.json','r',encoding='utf-8-sig').read()
fgp.add_child(folium.GeoJson(data= (geoData),
                            style_function = lambda x:{'fillColor':'green' 
                                                       if x['properties']['POP2005']<10000000 else 'yellow' 
                                                       if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fgv)

map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
