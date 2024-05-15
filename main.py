import requests

API_KEY = "80fe266478d54a2aa729dde5f78fe974"
url = "https://newsapi.org/v2/top-headlines/sources?apiKey="+API_KEY

req = requests.get(url)
content = req.text
print(content)
