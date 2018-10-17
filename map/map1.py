import folium
import pandas

the_map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Mapbox Bright")


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def elev_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"
fgv = folium.FeatureGroup(name="Volcanoes")


for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(
        folium.CircleMarker(location=[lt, ln], popup=str(el) + " m", fill=True, radius=6, fill_color=elev_color(el),
                            color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                            style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10_000_000
                            else "orange" if 10_000_000 <= x["properties"]["POP2005"] < 20_000_000 else "red"}))

the_map.add_child(fgv)
the_map.add_child(fgp)

the_map.add_child(folium.LayerControl())
the_map.save("Map1.html")
