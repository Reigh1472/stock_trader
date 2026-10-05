import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://openapivts.koreainvestment.com:29443/oauth2/tokenP"
body = {
    "grant_type": "client_credentials",
    "appkey": os.environ["KIS_APP_KEY"],
    "appsecret": os.environ["KIS_APP_SECRET"],
}

r = requests.post(url, json=body)
data = r.json()

print("status:", r.status_code)
if "access_token" in data:
    print("OK: token received")
else:
    print("FAILED:", data)
