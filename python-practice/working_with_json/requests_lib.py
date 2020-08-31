import requests # pip install requests. Remember to not name a file the same as an import
import json

posts = requests.get('https://jsonplaceholder.typicode.com/posts')
print(type(posts)) # requests.models.Response

# docs is now a response byte object, and has a number of accessible utilities
# .text .url .headers
print(f'URL: {posts.url}')
print(f'Status code: {posts.status_code}')
print(f'Headers: {posts.headers}')

posts = posts.text # remember to convert to text with the .text utility
posts = json.loads(posts) 
print(type(posts)) # list

#print(json.dumps(posts[0:3], indent=2))



### Tutorial ###
r = requests.get('https://imgs.xkcd.com/comics/python.png')

#with open('comic.png', 'wb') as f:
#  f.write(r.content)

