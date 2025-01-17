import time
import requests
from bs4 import BeautifulSoup

target_url = "https://type.jp/rank/"

def scrape_ranking_urls(target_url, sleep_sec=1, top_n=20):
    response = requests.get(target_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # 「a[href][data-way='39']」をリストに格納
    ranking_items = soup.select('a[href][data-way="39"]')

    ranking_urls = []
    for item in ranking_items:
        url = item.get('href')
        if url:
            # 相対パスの場合の補完
            if url.startswith('/'):
                url = "https://type.jp/" + url

            # 重複チェック
            if url not in ranking_urls:
                ranking_urls.append(url)

    # ここで先頭 top_n 件だけに絞る
    ranking_urls_top = ranking_urls[:20]

    print(f"\n=== {target_url} の上位 {top_n} 件 ===")

    # 順番に表示
    for idx, url in enumerate(ranking_urls_top, start=1):
        print(f"{idx}位: {url}")

    # スリープ（サイトに負荷をかけすぎないように）
    time.sleep(1)

    return ranking_urls_top


def main():
    base = "https://type.jp/rank/"

    paths = [
        "",
        "development/",
        "pm/",
        "infrastructure/",
        "engineer/",
        "sales/",
        "service/",
        "office/",
        "others/"
    ]

    all_scraped_urls = []

    for path in paths:
        # path が空文字のときは https://type.jp/rank/
        # path が 'job-1' のときは https://type.jp/rank/job-1/
        # などに変換
        if path == "":
            target_url = base  # "https://type.jp/rank/"
        else:
            # 末尾に / をつけておく
            target_url = base.rstrip('/') + "/" + path.strip('/') + "/"

        # 1～20位のURLを取得
        urls_top20 = scrape_ranking_urls(target_url, sleep_sec=1, top_n=20)

        # 取得したURLをまとめてリストに追加
        all_scraped_urls.extend(urls_top20)

    print("\n=== まとめて取得した全URL ===")
    for url in all_scraped_urls:
        print(url)


if __name__ == '__main__':
    main()






