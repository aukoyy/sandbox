import json

obj = ['foo', {'bar': ('baz', None, 1.0,2)}]
print(type(obj)) # list

# To encode a python dictionary or list, use json.dumps(object)
# This will produce a string form in json format
dump = json.dumps(obj)

print(dump)
print(type(dump)) # str