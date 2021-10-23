import json
k='{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(k)
json_obj = json.loads(k)
print("Unique Key in a JSON object:")
print(json_obj) 


