import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'if-modified-since': 'Sat, 03 May 2025 09:40:26 GMT',
    'if-none-match': 'W/"6815e48a-358846"',
    'origin': 'https://www.youbike.com.tw',
    'priority': 'u=1, i',
    'referer': 'https://www.youbike.com.tw/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

response = requests.get('https://apis.youbike.com.tw/json/station-min-yb2.json', headers=headers)
response.json()