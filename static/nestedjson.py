import csv
import json
output = { 'state':[] }
with open('county_state.csv', 'rU') as csv_file:
    for state_name in csv.DictReader(csv_file):
        output['state'].append({
            'fips': state_name['fips2'],
            'county': '%s - %s' % (state_name['state_name'],  state_name['county_name'])

        })

print json.dumps(output)
