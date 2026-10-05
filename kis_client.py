import json
import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

BASE = "https://openapivts.koreainvestment.com:29443"
TOKEN_FILE = "kis_token.json"


def get_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE) as f:
            saved = json.load(f)
        if saved["expires_at"] > time.time():
            return saved["token"]

    body = {
        "grant_type": "client_credentials",
        "appkey": os.environ["KIS_APP_KEY"],
        "appsecret": os.environ["KIS_APP_SECRET"],
    }
    data = requests.post(BASE + "/oauth2/tokenP", json=body).json()
    saved = {
        "token": data["access_token"],
        "expires_at": time.time() + data["expires_in"] - 300,
    }
    with open(TOKEN_FILE, "w") as f:
        json.dump(saved, f)
    return saved["token"]


def get_price(code):
    headers = {
        "authorization": "Bearer " + get_token(),
        "appkey": os.environ["KIS_APP_KEY"],
        "appsecret": os.environ["KIS_APP_SECRET"],
        "tr_id": "FHKST01010100",
    }
    params = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": code}
    url = BASE + "/uapi/domestic-stock/v1/quotations/inquire-price"
    return requests.get(url, headers=headers, params=params).json()


if __name__ == "__main__":
    result = get_price("005930")
    print(result.get("rt_cd"), result.get("msg1"))
    print("Samsung price:", result.get("output", {}).get("stck_prpr"))
