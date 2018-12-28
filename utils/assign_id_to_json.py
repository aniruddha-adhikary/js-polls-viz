import json
import os

with open(os.path.join(os.getcwd(), '..', 'data', 'districts.json')) as f: 
    data = json.load(f)

def assign_id(d): 
    d['id'] = d['properties']['ADM2_EN']

for feature in data['features']:
    assign_id(feature)

with open(os.path.join(os.getcwd(), '..', 'data', 'districts_amended.json'), 'w') as f: 
    json.dump(data, f)
