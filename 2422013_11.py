import pandas as pd
import numpy as np

# CSVファイルの読み込み
users = pd.read_csv('users.csv')
orders = pd.read_csv('orders.csv')
items = pd.read_csv('items.csv')

# orders と items を item_id でマージして商品価格を取得
orders_items = orders.merge(items, on='item_id')

# 各注文行の購入金額を計算
orders_items['purchase_amount'] = orders_items['order_num'] * orders_items['item_price']

# user_id ごとに購入金額の平均を計算
user_avg_purchase = orders_items.groupby('user_id')['purchase_amount'].mean().reset_index()

# 最も高い平均購入金額のユーザを特定
max_user = user_avg_purchase.loc[user_avg_purchase['purchase_amount'].idxmax()]

# numpy型から標準のPython型に変換
user_id = int(max_user['user_id'])
average_purchase_amount = float(max_user['purchase_amount'])

# 結果を出力
print([user_id, average_purchase_amount])