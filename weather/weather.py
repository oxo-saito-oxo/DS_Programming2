import flet as ft
import requests
import datetime

AREA_JSON_URL = "https://www.jma.go.jp/bosai/common/const/area.json"
FORECAST_URL_TEMPLATE = "https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"

# 天気コードと対応する天気のマッピング
WEATHER_CODES = {
    '100': '晴れ',
    '101': '晴れ 時々 くもり',
    '102': '晴れ 一時 雨',
    '103': '晴れ 時々 雨',
    '104': '晴れ 一時 雪',
    '105': '晴れ 時々 雪',
    '106': '晴れ 一時 雨か雪',
    '107': '晴れ 時々 雨か雪',
    '108': '晴れ 一時 雨か雷雨',
    '110': '晴れ のち時々くもり',
    '111': '晴れ のち くもり',
    '112': '晴れ のち一時 雨',
    '113': '晴れ のち時々 雨',
    '114': '晴れ のち 雨',
    '115': '晴れ のち一時 雪',
    '116': '晴れ のち時々 雪',
    '117': '晴れ のち 雪',
    '118': '晴れ のち 雨か雪',
    '119': '晴れ のち 雨か雷雨',
    '120': '晴れ 朝夕 一時 雨',
    '121': '晴れ 朝の内一時 雨',
    '122': '晴れ 夕方一時 雨',
    '123': '晴れ 山沿い 雷雨',
    '124': '晴れ 山沿い 雪',
    '125': '晴れ 午後は雷雨',
    '126': '晴れ 昼頃から雨',
    '127': '晴れ 夕方から雨',
    '128': '晴れ 夜は雨',
    '129': '晴れ 夜半から雨',
    '130': '朝の内 霧 後 晴れ',
    '131': '晴れ 明け方 霧',
    '132': '晴れ 朝夕 くもり',
    '140': '晴れ 時々 雨で雷を伴う',
    '160': '晴れ 一時 雪か雨',
    '170': '晴れ 時々 雪か雨',
    '181': '晴れ のち 雪か雨',
    '200': 'くもり',
    '201': 'くもり 時々 晴れ',
    '202': 'くもり 一時 雨',
    '203': 'くもり 時々 雨',
    '204': 'くもり 一時 雪',
    '205': 'くもり 時々 雪',
    '206': 'くもり 一時 雨か雪',
    '207': 'くもり 時々 雨か雪',
    '208': 'くもり 一時 雨か雷雨',
    '209': '霧',
    '210': 'くもり のち時々 晴れ',
    '211': 'くもり のち 晴れ',
    '212': 'くもり のち一時 雨',
    '213': 'くもり のち時々 雨',
    '214': 'くもり のち 雨',
    '215': 'くもり のち一時 雪',
    '216': 'くもり のち時々 雪',
    '217': 'くもり のち 雪',
    '218': 'くもり のち 雨か雪',
    '219': 'くもり のち 雨か雷雨',
    '220': 'くもり 朝夕一時 雨',
    '221': 'くもり 朝の内一時 雨',
    '222': 'くもり 夕方一時 雨',
    '223': 'くもり 日中時々 晴れ',
    '224': 'くもり 昼頃から雨',
    '225': 'くもり 夕方から雨',
    '226': 'くもり 夜は雨',
    '227': 'くもり 夜半から雨',
    '228': 'くもり 昼頃から雪',
    '229': 'くもり 夕方から雪',
    '230': 'くもり 夜は雪',
    '231': 'くもり海上海岸は霧か霧雨',
    '240': 'くもり 時々雨で 雷を伴う',
    '250': 'くもり 時々雪で 雷を伴う',
    '260': 'くもり 一時 雪か雨',
    '270': 'くもり 時々 雪か雨',
    '281': 'くもり のち 雪か雨',
    '300': '雨',
    '301': '雨 時々 晴れ',
    '302': '雨 時々 止む',
    '303': '雨 時々 雪',
    '304': '雨か雪',
    '306': '大雨',
    '307': '風雨共に強い',
    '308': '雨で暴風を伴う',
    '309': '雨 一時 雪',
    '311': '雨 のち 晴れ',
    '313': '雨 のち くもり',
    '314': '雨 のち時々 雪',
    '315': '雨 のち 雪',
    '316': '雨か雪 のち 晴れ',
    '317': '雨か雪 のち くもり',
    '320': '朝の内雨 のち 晴れ',
    '321': '朝の内雨 のち くもり',
    '322': '雨 朝晩一時 雪',
    '323': '雨 昼頃から 晴れ',
    '324': '雨 夕方から 晴れ',
    '325': '雨 夜は晴',
    '326': '雨 夕方から雪',
    '327': '雨 夜は雪',
    '328': '雨 一時強く降る',
    '329': '雨 一時 みぞれ',
    '340': '雪か雨',
    '350': '雨で雷を伴う',
    '361': '雪か雨 のち 晴れ',
    '371': '雪か雨 のち くもり',
    '400': '雪',
    '401': '雪 時々 晴れ',
    '402': '雪 時々止む',
    '403': '雪 時々 雨',
    '405': '大雪',
    '406': '風雪強い',
    '407': '暴風雪',
    '409': '雪 一時 雨',
    '411': '雪 のち 晴れ',
    '413': '雪 のち くもり',
    '414': '雪 のち 雨',
    '420': '朝の内雪 のち 晴れ',
    '421': '朝の内雪 のち くもり',
    '422': '雪 昼頃から雨',
    '423': '雪 夕方から雨',
    '424': '雪 夜半から雨',
    '425': '雪 一時強く降る',
    '426': '雪 のち みぞれ',
    '427': '雪 一時 みぞれ',
    '450': '雪で雷を伴う'
}


def get_area_info():
    try:
        response = requests.get(AREA_JSON_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve area information: {e}")
        return None

def get_weather_forecast(area_code):
    url = FORECAST_URL_TEMPLATE.format(area_code=area_code)
    print(f"Fetching weather data from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("Weather data:", data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve weather forecast for area code {area_code}: {e}")
        return None

def build_list_tiles(region, on_select, regions_data):
    list_tiles = []
    for prefecture, details in regions_data.get(region, {}).items():
        area_code = details['code']
        list_tile = ft.ListTile(
            title=ft.Text(prefecture),
            on_click=lambda e, code=area_code, name=prefecture: on_select(e, code, name)
        )
        list_tiles.append(list_tile)
    return list_tiles

def main(page: ft.Page):
    page.title = "天気予報アプリ"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    region_label = ft.Text(value="地方を選択してください", size=20)
    weather_container = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    prefecture_list = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    regions_data = None

    def on_region_change(e):
        selected_region = JAPAN_REGIONS_KEYS[e.control.selected_index]
        region_label.value = f"{selected_region}の都道府県を選択してください"
        list_tiles = build_list_tiles(selected_region, on_prefecture_select, regions_data)
        prefecture_list.controls = list_tiles
        prefecture_list.update()
        weather_container.controls.clear()
        weather_container.update()

    def on_prefecture_select(e, area_code, prefecture_name):
        region_label.value = f"{prefecture_name}の天気情報を読み込み中..."
        page.update()
        weather_container.controls.clear()
        weather_container.update()

        data = get_weather_forecast(area_code)
        if data:
            region_label.value = f"{prefecture_name}の天気情報"
            weather_container.controls.clear()
            try:
                time_series = data[0]["timeSeries"]
                weather_areas = time_series[0]["areas"]

                temps_min = temps_max = None
                if len(time_series) > 1:
                    for series in time_series:
                        if "tempsMin" in series["areas"][0]:
                            temps_min = series["areas"][0].get("tempsMin")
                        if "tempsMax" in series["areas"][0]:
                            temps_max = series["areas"][0].get("tempsMax")

                for i, time in enumerate(time_series[0]["timeDefines"][:2]):
                    date = datetime.datetime.strptime(time.split("T")[0], "%Y-%m-%d").strftime("%Y-%m-%d")
                    weather_code = weather_areas[0]["weatherCodes"][i] if i < len(weather_areas[0]["weatherCodes"]) else "999"
                    weather = WEATHER_CODES.get(weather_code, f"天気コード {weather_code}")

                    temp_min = temps_min[i] if temps_min and temps_min[i] is not None else None
                    temp_max = temps_max[i] if temps_max and temps_max[i] is not None else None

                    temp_texts = []
                    if temp_min is not None:
                        temp_texts.append(ft.Text(f"最低気温: {temp_min}℃", size=15, color=ft.colors.BLUE))
                    if temp_max is not None:
                        temp_texts.append(ft.Text(f"最高気温: {temp_max}℃", size=15, color=ft.colors.RED))

                    forecast_card = ft.Container(
                        content=ft.Column([
                            ft.Text(f"日付: {date}", size=15, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                            ft.Text(f"天気: {weather}", size=15, color=ft.colors.BLACK),
                            ft.Image(src=f"https://www.jma.go.jp/bosai/forecast/img/{weather_code}.svg", width=50, height=50),
                            *temp_texts
                        ]),
                        padding=10,
                        border_radius=10,
                        bgcolor=ft.colors.WHITE,
                        alignment=ft.alignment.center,
                        width=300,
                        height=150  # 高さ調整
                    )
                    weather_container.controls.append(forecast_card)
            except Exception as e:
                print(f"Error processing weather data: {e}")
                region_label.value = "天気情報の処理中にエラーが発生しました。"
        else:
            region_label.value = "天気情報が取得できませんでした。"
        region_label.update()
        weather_container.update()

    area_info = get_area_info()
    if not area_info:
        page.add(ft.Text(value="エリア情報の取得に失敗しました。"))
        return

    regions_data = {
        "北海道": {},
        "東北": {},
        "関東": {},
        "中部": {},
        "近畿": {},
        "中国": {},
        "四国": {},
        "九州・沖縄": {}
    }

    region_mappings = {
        "010000": "北海道",
        "020000": "東北",
        "030000": "東北",
        "040000": "東北",
        "050000": "東北",
        "060000": "東北",
        "070000": "東北",
        "080000": "関東",
        "090000": "関東",
        "100000": "関東",
        "110000": "関東",
        "120000": "関東",
        "130000": "関東",
        "140000": "関東",
        "150000": "中部",
        "160000": "中部",
        "170000": "中部",
        "180000": "中部",
        "190000": "中部",
        "200000": "中部",
        "210000": "中部",
        "220000": "中部",
        "230000": "中部",
        "240000": "近畿",
        "250000": "近畿",
        "260000": "近畿",
        "270000": "近畿",
        "280000": "近畿",
        "290000": "近畿",
        "300000": "近畿",
        "310000": "中国",
        "320000": "中国",
        "330000": "中国",
        "340000": "中国",
        "350000": "中国",
        "360000": "四国",
        "370000": "四国",
        "380000": "四国",
        "390000": "四国",
        "400000": "九州・沖縄",
        "410000": "九州・沖縄",
        "420000": "九州・沖縄",
        "430000": "九州・沖縄",
        "440000": "九州・沖縄",
        "450000": "九州・沖縄",
        "460000": "九州・沖縄",
        "470000": "九州・沖縄"
    }

    for area_code, details in area_info["offices"].items():
        region = region_mappings.get(area_code[:2] + "0000")
        if region:
            regions_data[region][details["name"]] = {"code": area_code}

    JAPAN_REGIONS_KEYS = list(regions_data.keys())

    side_nav = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        leading=ft.Text("地域選択"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(label=region, icon=ft.icons.CLOUD, selected_icon=ft.icons.CLOUD_QUEUE)
            for region in JAPAN_REGIONS_KEYS
        ],
        on_change=on_region_change,
        expand=True  # NavigationRailの高さを設定
    )

    page.add(
        ft.Row([
            ft.Container(
                ft.Column([
                    side_nav,
                ], expand=True),
                width=100,
            ),
            ft.Container(
                ft.Column([
                    prefecture_list,
                ], expand=True),
                width=300,
            ),
            ft.Container(
                ft.Column([
                    region_label,
                    weather_container,
                ], expand=True),
                width=800,
            )
        ], expand=True)
    )

    initial_event = type("Event", (object,), {"control": type("Control", (object,), {"selected_index": 0})})
    on_region_change(initial_event())

ft.app(target=main)