import pandas as pd

# CSVファイルの読み込み
users = pd.read_csv('users.csv')
orders = pd.read_csv('orders.csv')
items = pd.read_csv('items.csv')

# ordersとitemsをitem_idでマージして商品価格を取得
orders_items = orders.merge(items, on='item_id')

# 各注文行の購入金額を計算
orders_items['purchase_amount'] = orders_items['order_num'] * orders_items['item_price']

# order_idごとに購入金額を合計
order_totals = orders_items.groupby('order_id')['purchase_amount'].sum()

# 最も高い購入金額の注文を特定
max_order_id = order_totals.idxmax()
max_purchase_amount = order_totals.max()

# 結果を出力
print([int(max_order_id), float(max_purchase_amount)])