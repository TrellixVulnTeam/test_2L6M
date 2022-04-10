from pandas import json_normalize

json = '{ "name": "Tanaka" }'

norm = json_normalize(json)
csv = norm.to_csv(path_or_buf=None)
print(csv)
