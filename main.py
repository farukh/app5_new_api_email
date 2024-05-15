import requests

API_KEY = "80fe266478d54a2aa729dde5f78fe974"
url = "https://newsapi.org/v2/everything?q=tesla&sortby=publishedAt&language=en&apiKey="+API_KEY

req = requests.get(url)
content = req.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])

