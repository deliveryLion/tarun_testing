import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')

data = r.json()

for d in data:
  print(d['userId'])
