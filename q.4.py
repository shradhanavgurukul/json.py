# Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

import json
a={
    '4':5,
    '6':7,
    '1':3,
    '2':4
}
k_json = json.dumps(a)
print(k_json)
k_json = json.dumps(a, sort_keys=True)
print(k_json)
