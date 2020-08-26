import json

load = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

print(type(load))
print(load) # list

print(type(load[1])) # dict

print(load[1].get('bar'))

