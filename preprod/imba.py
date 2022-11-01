import folium, geopandas, branca
from folium.plugins import Search


states = geopandas.read_file(
    # "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json",
    # "datalist.json",
    # "square.json",
    "test.json",
    driver="GeoJSON",
)

cities = geopandas.read_file(
    # "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_populated_places_simple.geojson",
    # "ao.geojson",
    "point.geojson",
    driver="GeoJSON",
)

states_sorted = states.sort_values(by="density", ascending=False)

states_sorted.head(5).append(states_sorted.tail(5))[["name", "density"]]

def rd2(x):
    return round(x, 2)


minimum, maximum = states["density"].quantile([0.05, 0.95]).apply(rd2)

mean = round(states["density"].mean(), 2)


print(f"minimum: {minimum}", f"maximum: {maximum}", f"Mean: {mean}", sep="\n\n")



colormap = branca.colormap.LinearColormap(
    colors=["#f2f0f7", "#cbc9e2", "#9e9ac8", "#756bb1", "#54278f"],
    index=states["density"].quantile([0.2, 0.4, 0.6, 0.8]),
    vmin=minimum,
    vmax=maximum,
)

colormap.caption = "Population Density in the United States"

us_cities = geopandas.sjoin(cities, states, how="inner", predicate="within")
# mo_cities = geopandas.sjoin(states, states, how="inner", predicate="within")
pop_ranked_cities = us_cities.sort_values(by="pop_max", ascending=False)[
    ["nameascii", "pop_max", "geometry"]
].iloc[:20]
print(pop_ranked_cities)
# pop_ranked_cities.head(5)
m = folium.Map(location=[56, 37], zoom_start=8)


def style_function(x):
    return {
        "fillColor": colormap(x["properties"]["density"]),
        "color": "black",
        "weight": 2,
        "fillOpacity": 0.5,
    }


stategeo = folium.GeoJson(
    states,
    name="US States",
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(
        fields=["name", "density"], aliases=["State", "Density"], localize=True
    ),
).add_to(m)

citygeo = folium.GeoJson(
    pop_ranked_cities,
    name="US Cities",
    tooltip=folium.GeoJsonTooltip(
        fields=["nameascii", "pop_max"], aliases=["", "Population Max"], localize=True
    ),
).add_to(m)

statesearch = Search(
    layer=stategeo,
    geom_type="Polygon",
    placeholder="Search for a US State",
    collapsed=False,
    search_label="name",
    weight=3,
).add_to(m)

citysearch = Search(
    layer=citygeo,
    geom_type="Point",
    placeholder="Search for a US City",
    collapsed=True,
    search_label="nameascii",
).add_to(m)

folium.LayerControl().add_to(m)
colormap.add_to(m)

m.save("imba.html")