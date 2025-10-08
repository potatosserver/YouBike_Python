import requests
import json

url = 'https://apis.youbike.com.tw/json/station-min-yb2.json'

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))

except Exception as e:
    print(f"發生未預期的錯誤: {e}")
