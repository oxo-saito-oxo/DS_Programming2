import flet as ft
import requests

def fetch_weather():
    # 東京都の都市コードを固定で利用
    city_code = "130000"
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{city_code}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException:
        return None

def main(page: ft.Page):
    page.title = "東京の天気予報"
    
    weather_info = ft.Text()
    
    def get_weather_data():
        data = fetch_weather()
        if data:
            forecast = data[0]["timeSeries"][0]["areas"][0]["weathers"][0]
            weather_info.value = f"東京の天気: {forecast}"
        else:
            weather_info.value = "天気情報の取得に失敗しました。"
        page.update()
    
    get_weather_data()
    
    # ページにウィジェットを追加
    page.add(weather_info)

ft.app(target=main)