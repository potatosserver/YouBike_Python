import requests
import json

def fetch_youbike_data():
    url = "https://apis.youbike.com.tw/json/station-min-yb2.json"
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
    }
    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except Exception as e:
        raise e

def search_site(query):
    data = fetch_youbike_data()
    valid_data = [site for site in data if isinstance(site, dict)]
    exact = [site for site in valid_data if site.get("station_no") == query]
    if exact:
        return exact
    return [site for site in valid_data if query in site.get("name_tw", "") or query in site.get("address_tw", "")]

def extract_station_info(site):
    return {
        "id": site.get("station_no"),
        "name": site.get("name_tw"),
        "coords": (site.get("lat"), site.get("lng")),
        "district": site.get("district_tw"),
        "address": site.get("address_tw")
    }

headers = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
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

def main():
    keyword = input("請輸入關鍵字 (站號、站名或地址，空白取得所有站點): ").strip()
    filter_ev = input("是否只顯示有電輔車的站點? (y/n): ").strip().lower().startswith('y')
    try:
        if keyword:
            raw_data = search_site(keyword)
        else:
            raw_data = fetch_youbike_data()
        stations = [extract_station_info(site) for site in raw_data]
        if len(stations) > 20:
            print("請縮小範圍")
            return
        station_ids = [station['id'] for station in stations]
        vehicle_data = query_vehicle_data(station_ids)
        found = False
        for station in stations:
            veh_data = vehicle_data.get(station['id'], {})
            detail = veh_data.get('available_spaces_detail', {})
            if filter_ev and int(detail.get('eyb', 0)) <= 0:
                continue
            print("站名:", station['name'])
            print("區域:", station['district'])
            print("地址:", station['address'])
            print("YouBike 2.0:", detail.get('yb2', '未知'))
            print("YouBike 2.0E:", detail.get('eyb', '未知'))
            print("可停空位數:", veh_data.get('empty_spaces', '未知'))
            print("-" * 40)
            found = True
        if not found:
            print("找不到符合條件的站點。")
    except Exception as e:
        print("發生錯誤:", e)

if __name__ == "__main__":
    main()