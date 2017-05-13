## Creates a dict file of station name mappings to id. This can be used to lookup an id based
## on station in order to call the by-id function

import json, sys

with open("stations.json", 'rb') as f:
    stations = json.load(f)
    for idx, station in enumerate(stations):
        station['id'] = idx
        print(str(station['id']) + "|" + str(station['name']).lower())
        