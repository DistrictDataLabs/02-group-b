import csv, itertools, json

def cluster(rows):
    result = []
    for key, group in itertools.groupby(rows, key=lambda r: r[0]):
        group_rows = [row[1:] for row in group]
        if len(group_rows[0]) == 2:
            result.append({key: dict(group_rows)})
        else:
            result.append({key: cluster(group_rows)})
    return result

if __name__ == '__main__':
    s = '''\
Gondwanaland,Bobs Bits,Operations,nuts,332
Gondwanaland,Bobs Bits,Operations,bolts,254
Gondwanaland,Maureens Melons,Operations,nuts,123
'''
    rows = list(csv.open('county_state.csv'))
    r = cluster(rows)
    print json.dumps(r, indent=4)
