import flet as ft

# 天気コードと画像URLの辞書
weather_data = {
    '100': ('晴れ', "https://www.jma.go.jp/bosai/forecast/img/100.svg"),
    '101': ('晴れ 時々 くもり', "https://www.jma.go.jp/bosai/forecast/img/101.svg"),
    '102': ('晴れ 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '103': ('晴れ 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '104': ('晴れ 一時 雪', "https://www.jma.go.jp/bosai/forecast/img/104.svg"),
    '105': ('晴れ 一時 雪', "https://www.jma.go.jp/bosai/forecast/img/104.svg"),
    '106': ('晴れ 一時 雨か雪', "https://www.jma.go.jp/bosai/forecast/img/104.svg"),
    '107': ('晴れ 一時 雨か雪', "https://www.jma.go.jp/bosai/forecast/img/104.svg"),
    '108': ('晴れ 一時 雨か雷雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '110': ('晴れ のち時々 くもり', "https://www.jma.go.jp/bosai/forecast/img/110.svg"),
    '111': ('晴れ のち くもり', "https://www.jma.go.jp/bosai/forecast/img/110.svg"),
    '112': ('晴れ のち一時 雨', "https://www.jma.go.jp/bosai/forecast/img/112.svg"),
    '113': ('晴れ のち一時 雨', "https://www.jma.go.jp/bosai/forecast/img/112.svg"),
    '114': ('晴れ のち 雨', "https://www.jma.go.jp/bosai/forecast/img/112.svg"),
    '115': ('晴れ のち一時 雪', "https://www.jma.go.jp/bosai/forecast/img/115.svg"),
    '116': ('晴れ のち一時 雪', "https://www.jma.go.jp/bosai/forecast/img/115.svg"),
    '117': ('晴れ のち 雪', "https://www.jma.go.jp/bosai/forecast/img/115.svg"),
    '118': ('晴れ のち 雨か雪', "https://www.jma.go.jp/bosai/forecast/img/115.svg"),
    '119': ('晴れ のち 雨か雷雨', "https://www.jma.go.jp/bosai/forecast/img/112.svg"),
    '120': ('晴れ 朝夕 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '121': ('晴れ 朝の内一時 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '122': ('晴れ 夕方一時 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '123': ('晴れ 山沿い 雷雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '124': ('晴れ 山沿い 雪', "https://www.jma.go.jp/bosai/forecast/img/104.svg"),
    '125': ('晴れ 午後は雷雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '126': ('晴れ 昼頃から 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '127': ('晴れ 夕方から 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '128': ('晴れ 夜は 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '129': ('晴れ 夜半から 雨', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '130': ('朝の内 霧 後 晴れ', "https://www.jma.go.jp/bosai/forecast/img/100.svg"),
    '131': ('晴れ 明け方 霧', "https://www.jma.go.jp/bosai/forecast/img/100.svg"),
    '132': ('晴れ 朝夕 くもり', "https://www.jma.go.jp/bosai/forecast/img/101.svg"),
    '140': ('晴れ 時々 雨で雷を伴う', "https://www.jma.go.jp/bosai/forecast/img/102.svg"),
    '160': ('晴れ 一時 雪か雨', "https://www.jma.go.jp/bosai/forecast/img/104.svg"),
    '170': ('晴れ 一時 雪か雨', "https://www.jma.go.jp/bosai/forecast/img/104.svg"),
    '181': ('晴れ のち 雪か雨', "https://www.jma.go.jp/bosai/forecast/img/115.svg"),
    '200': ('くもり', "https://www.jma.go.jp/bosai/forecast/img/200.svg"),
    '201': ('くもり 時々 晴れ', "https://www.jma.go.jp/bosai/forecast/img/201.svg"),
    '202': ('くもり 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '203': ('くもり 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '204': ('くもり 一時 雪', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '205': ('くもり 一時 雪', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '206': ('くもり 一時 雨か雪', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '207': ('くもり 一時 雨か雪', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '208': ('くもり 一時 雨か雷雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '209': ('霧', "https://www.jma.go.jp/bosai/forecast/img/200.svg"),
    '210': ('くもり のち 時々 晴れ', "https://www.jma.go.jp/bosai/forecast/img/210.svg"),
    '211': ('くもり のち 晴れ', "https://www.jma.go.jp/bosai/forecast/img/210.svg"),
    '212': ('くもり のち 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/212.svg"),
    '213': ('くもり のち 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/212.svg"),
    '214': ('くもり のち 雨', "https://www.jma.go.jp/bosai/forecast/img/212.svg"),
    '215': ('くもり のち 一時 雪', "https://www.jma.go.jp/bosai/forecast/img/215.svg"),
    '216': ('くもり のち 一時 雪', "https://www.jma.go.jp/bosai/forecast/img/215.svg"),
    '217': ('くもり のち 雪', "https://www.jma.go.jp/bosai/forecast/img/215.svg"),
    '218': ('くもり のち 雨か雪', "https://www.jma.go.jp/bosai/forecast/img/215.svg"),
    '219': ('くもり のち 雨か雷雨', "https://www.jma.go.jp/bosai/forecast/img/212.svg"),
    '220': ('くもり 朝夕 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '221': ('くもり 朝の内一時 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '222': ('くもり 夕方 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '223': ('くもり 日中 時々 晴れ', "https://www.jma.go.jp/bosai/forecast/img/201.svg"),
    '224': ('くもり 昼頃から 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '225': ('くもり 夕方から 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '226': ('くもり 夜は 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '227': ('くもり 夜半から 雨', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '228': ('くもり 昼頃から 雪', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '229': ('くもり 夕方から 雪', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '230': ('くもり 夜は 雪', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '231': ('くもり 海上海岸は霧か霧雨', "https://www.jma.go.jp/bosai/forecast/img/200.svg"),
    '240': ('くもり 時々 雨で雷を伴う', "https://www.jma.go.jp/bosai/forecast/img/202.svg"),
    '250': ('くもり 時々 雪で雷を伴う', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '260': ('くもり 一時 雪か雨', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '270': ('くもり 一時 雪か雨', "https://www.jma.go.jp/bosai/forecast/img/204.svg"),
    '281': ('くもり のち 雪か雨', "https://www.jma.go.jp/bosai/forecast/img/215.svg"),
    '300': ('雨', "https://www.jma.go.jp/bosai/forecast/img/300.svg"),
    '301': ('雨 時々 晴れ', "https://www.jma.go.jp/bosai/forecast/img/301.svg"),
    '302': ('雨 時々止む', "https://www.jma.go.jp/bosai/forecast/img/302.svg"),
    '303': ('雨 時々 雪', "https://www.jma.go.jp/bosai/forecast/img/303.svg"),
    '304': ('雨か雪', "https://www.jma.go.jp/bosai/forecast/img/303.svg"),
    '306': ('大雨', "https://www.jma.go.jp/bosai/forecast/img/300.svg"),
    '307': ('風雨共に強い', "https://www.jma.go.jp/bosai/forecast/img/300.svg"),
    '308': ('雨で暴風を伴う', "https://www.jma.go.jp/bosai/forecast/img/308.svg"),
    '309': ('雨 一時 雪', "https://www.jma.go.jp/bosai/forecast/img/303.svg"),
    '311': ('雨 のち 晴れ', "https://www.jma.go.jp/bosai/forecast/img/311.svg"),
    '313': ('雨 のち くもり', "https://www.jma.go.jp/bosai/forecast/img/313.svg"),
    '314': ('雨 のち 時々 雪', "https://www.jma.go.jp/bosai/forecast/img/314.svg"),
    '315': ('雨 のち 雪', "https://www.jma.go.jp/bosai/forecast/img/314.svg"),
    '316': ('雨か雪 のち 晴れ', "https://www.jma.go.jp/bosai/forecast/img/311.svg"),
    '317': ('雨か雪 のち くもり', "https://www.jma.go.jp/bosai/forecast/img/313.svg"),
    '320': ('朝の内雨 のち 晴れ', "https://www.jma.go.jp/bosai/forecast/img/311.svg"),
    '321': ('朝の内雨 のち くもり', "https://www.jma.go.jp/bosai/forecast/img/313.svg"),
    '322': ('雨 朝晩 一時 雪', "https://www.jma.go.jp/bosai/forecast/img/303.svg"),
    '323': ('雨 昼頃から 晴れ', "https://www.jma.go.jp/bosai/forecast/img/311.svg"),
    '324': ('雨 夕方から 晴れ', "https://www.jma.go.jp/bosai/forecast/img/311.svg"),
    '325': ('雨 夜は 晴', "https://www.jma.go.jp/bosai/forecast/img/311.svg"),
    '326': ('雨 夕方から 雪', "https://www.jma.go.jp/bosai/forecast/img/303.svg"),
    '327': ('雨 夜は 雪', "https://www.jma.go.jp/bosai/forecast/img/303.svg"),
    '328': ('雨 一時強く降る', "https://www.jma.go.jp/bosai/forecast/img/300.svg"),
    '329': ('雨 一時 みぞれ', "https://www.jma.go.jp/bosai/forecast/img/303.svg"),
    '340': ('雪か雨', "https://www.jma.go.jp/bosai/forecast/img/303.svg"),
    '350': ('雨で雷を伴う', "https://www.jma.go.jp/bosai/forecast/img/300.svg"),
    '361': ('雪か雨 のち 晴れ', "https://www.jma.go.jp/bosai/forecast/img/311.svg"),
    '371': ('雪か雨 のち くもり', "https://www.jma.go.jp/bosai/forecast/img/313.svg"),
    '400': ('雪', "https://www.jma.go.jp/bosai/forecast/img/400.svg"),
    '401': ('雪 時々 晴れ', "https://www.jma.go.jp/bosai/forecast/img/401.svg"),
    '402': ('雪 時々止む', "https://www.jma.go.jp/bosai/forecast/img/402.svg"),
    '403': ('雪 時々 雨', "https://www.jma.go.jp/bosai/forecast/img/403.svg"),
    '405': ('大雪', "https://www.jma.go.jp/bosai/forecast/img/400.svg"),
    '406': ('風雪強い', "https://www.jma.go.jp/bosai/forecast/img/406.svg"),
    '407': ('暴風雪', "https://www.jma.go.jp/bosai/forecast/img/406.svg"),
    '409': ('雪 一時 雨', "https://www.jma.go.jp/bosai/forecast/img/403.svg"),
    '411': ('雪 のち 晴れ', "https://www.jma.go.jp/bosai/forecast/img/411.svg"),
    '413': ('雪 のち くもり', "https://www.jma.go.jp/bosai/forecast/img/413.svg"),
    '414': ('雪 のち 雨', "https://www.jma.go.jp/bosai/forecast/img/414.svg"),
    '420': ('朝の内雪 のち 晴れ', "https://www.jma.go.jp/bosai/forecast/img/411.svg"),
    '421': ('朝の内雪 のち くもり', "https://www.jma.go.jp/bosai/forecast/img/413.svg"),
    '422': ('雪 昼頃から 雨', "https://www.jma.go.jp/bosai/forecast/img/414.svg"),
    '423': ('雪 夕方から 雨', "https://www.jma.go.jp/bosai/forecast/img/414.svg"),
    '424': ('雪 夜半から 雨', "https://www.jma.go.jp/bosai/forecast/img/414.svg"),
    '425': ('雪 一時強く降る', "https://www.jma.go.jp/bosai/forecast/img/400.svg"),
    '426': ('雪 のち みぞれ', "https://www.jma.go.jp/bosai/forecast/img/403.svg"),
    '427': ('雪 一時 みぞれ', "https://www.jma.go.jp/bosai/forecast/img/403.svg"),
    '450': ('雪で雷を伴う', "https://www.jma.go.jp/bosai/forecast/img/400.svg")
}

def main(page: ft.Page):

    # 表示したい天気コード
    weather_code = '100'  # 例: '100'を指定

    if weather_code in weather_data:
        description, url = weather_data[weather_code]
        image = ft.Image(src=url, width=50, height=50)

        page.add(ft.Text(f"天気コード {weather_code}: {description}"))
        page.add(image)
    else:
        page.add(ft.Text(f"天気コード {weather_code} が見つかりませんでした。"))

ft.app(target=main)