from urllib.request import urlopen
import json

target_url = 'https://covid19-update-api.herokuapp.com/api/v1/cases/active'
data = urlopen(target_url)
print(type(data)) # http.client.HTTPResponse
data = data.read().decode()
print(type(data)) # str
data = json.loads(data)
print(type(data)) # dict