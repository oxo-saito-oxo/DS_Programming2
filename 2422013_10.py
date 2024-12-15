import pandas as pd

# CSVファイルの読み込み
items = pd.read_csv('items.csv')
orders = pd.read_csv('orders.csv')

# ordersとitemsを結合
merged = pd.merge(orders, items, on='item_id')

# 合計金額を計算
merged['total_price'] = merged['order_num'] * merged['item_price']

# 各注文の合計価格を計算し、user_idでグループ化して、平均購入金額を計算
average_purchase = merged.groupby('user_id')['total_price'].mean().reset_index()

# 最も高い平均購入金額のユーザーを見つける
max_average_purchase = average_purchase.loc[average_purchase['total_price'].idxmax()]

# 結果を出力
print([max_average_purchase['user_id'], max_average_purchase['total_price']])