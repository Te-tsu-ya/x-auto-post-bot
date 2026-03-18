import os
import requests
from requests_oauthlib import OAuth1

# 認証情報
API_KEY = os.environ["X_API_KEY"]
API_SECRET = os.environ["X_API_SECRET"]
ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["X_ACCESS_SECRET"]

# news.txt読み込み
with open("news.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 認証
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# 投稿
url = "https://api.twitter.com/2/tweets"
response = requests.post(
    url,
    auth=auth,
    json={"text": text}
)

print(response.status_code)
print(response.text)
