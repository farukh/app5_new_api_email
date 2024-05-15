import requests
from send_email import send_email;

API_KEY = "80fe266478d54a2aa729dde5f78fe974"
category ="pakistan hockey"
url = ("https://newsapi.org/v2/everything?"
       f"q={category}&"
       "sortby=publishedAt&"
       "language=en&"
       "apiKey=")+API_KEY

req = requests.get(url)
content = req.json()
content_email = "Subject: News Api Emails\n"
for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None:
        content_email = (content_email + article['title'] + "\n"
        + article['description'] + article['url'] + 2*"\n")

content_email = content_email.encode('utf-8')

try:
    print(content_email)
    send_email(content_email)

except Exception as e:
    print("ERROR : "+str(e))

