import os
import requests
from requests_oauthlib import OAuth1

# 認証情報
API_KEY = os.environ["nmUwDQj0KcHlsV714xjZ8jPBj"]#X_API_KEY
API_SECRET = os.environ["UK38G4e5wF1g0He1nHnm8ESz32ubezdWD7KAZrc2avtPlpXGZK"]#X_API_SECRET
ACCESS_TOKEN = os.environ["1796341683959083009-eq5lViJ76PdXYQ4tuzdwhGI1mLM0z4"]#X_ACCESS_TOKEN
ACCESS_SECRET = os.environ["hs2BVReuEKhS3gpIPJ6oX8t4Es7Zc8Yd7FoUGy0ucpIUt"]#X_ACCESS_SECRET

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
