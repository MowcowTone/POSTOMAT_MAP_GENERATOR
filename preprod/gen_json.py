from create import generat as g
from types import SimpleNamespace
import json

def gen_json(id, name, density, pop_min, coordinates):

    # id, name, density, pop_min, coordinates
    # props
    # id = str
    # name = str
    # density = int
    # pop_min = int
    FeatureCollection = "FeatureCollection"
    Feature = "Feature"
    MultiPolygon = "MultiPolygon"

    # JSon object
    # lists
    jsondata = {}
    features = [{}]
    properties = {}
    geometry = {}
    # props to lists
    features[0]["type"] = Feature 
    features[0]["id"] = id

    properties['name'] = name
    properties['density'] = density
    properties['pop_min'] = pop_min
    features[0]['properties'] = properties


    geometry["type"] = MultiPolygon
    geometry["coordinates"] = coordinates 
    features[0]["geometry"] = geometry

    jsondata["type"] = FeatureCollection
    jsondata["features"] = features
    dump = json.dumps(jsondata)

    print(dump)


    with open('test.json', 'w') as f:
        f.write(dump)
x=2 ####размер
y=2
squares = g.squares(x,y)
points = g.points(x,y)
gen_json("25", "name", 20, 30, [[[
              [37.03, 56.015],
              [37.03, 56.0],
              [37.0, 56.0],
              [37.0, 56.015]
            ]]])