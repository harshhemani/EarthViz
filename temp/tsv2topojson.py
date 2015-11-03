from __future__ import print_function

import sys
import json

if len(sys.argv) < 3:
    print("\nSyntax:\n\tpython {} <path-to-tsv-file> <output-file-path>\n".format(sys.argv[0]))
    sys.exit(1)

tsvfilepath = sys.argv[1]
outfilepath = sys.argv[2]
lines = open(tsvfilepath, 'r').readlines()

result = {}
result['type'] = 'LineString'
result['coordinates'] = []
for line in lines:
    line = line.strip()
    lon, lat = line.split()
    lon = float(lon)
    lat = float(lat)
    result['coordinates'].append([lon, lat])
json.dump(result, open(outfilepath, 'w'))
