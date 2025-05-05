import requests
import json

headers = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
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

def query_vehicle_data(station_ids):
    data = '{"station_no":' + json.dumps(station_ids) + '}'
    response = requests.post('https://apis.youbike.com.tw/tw2/parkingInfo', headers=headers, data=data)
    result = response.json()
    ret_val = result.get("retVal", {})
    if isinstance(ret_val, list):
        data_array = ret_val
    else:
        data_array = ret_val.get("data", [])
    data_array = [item for item in data_array if isinstance(item, dict)]
    vehicle_data = {item.get("station_no"): item for item in data_array}
    return vehicle_data

if __name__ == "__main__":
    sample_station_ids = [501210134, 501210084]  # 範例站點編號
    result = query_vehicle_data(sample_station_ids)
    print(json.dumps(result, ensure_ascii=False, indent=2))