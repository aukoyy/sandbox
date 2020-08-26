import json

obj = ['foo', {'bar': ('baz', None, 1.0,2)}]
print(type(obj)) # list

dump = json.dumps(obj)

print(dump)
print(type(dump)) # str