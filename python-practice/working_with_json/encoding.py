import json

obj = ['foo', {'bar': ('baz', None, 1.0,2)}]
print(type(obj)) # list

# To encode a python dictionary or list, use json.dumps(object)
# This will produce a string form in json format
dump = json.dumps(obj)

print(dump)
print(type(dump)) # str


# To format with indentation, use indent=2
formatted_dump = json.dumps(obj, indent=2)
print('\n Indented:')
print(formatted_dump)


# loads() is for string, load() is for file