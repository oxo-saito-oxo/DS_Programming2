import pandas as pd
import numpy as np

# CSVファイルの読み込み
items = pd.read_csv('items.csv')

# 対象商品の取得（item_idが101）
target_item_id = 101
target_item = items[items['item_id'] == target_item_id]

if target_item.empty:
    print(f"item_id {target_item_id} がitems.csvに存在しません。")
    exit()

target_item = target_item.iloc[0]
target_small_category = target_item['small_category']
target_big_category = target_item['big_category']
target_item_price = target_item['item_price']
target_page_num = target_item['page_num']

# 対象商品を除外して推薦候補を準備
recommend_candidates = items[items['item_id'] != target_item_id].copy()

# カテゴリの類似性を計算
def calculate_category_similarity(row):
    if row['small_category'] == target_small_category:
        return 2
    elif row['big_category'] == target_big_category:
        return 1
    else:
        return 0

recommend_candidates['category_similarity'] = recommend_candidates.apply(calculate_category_similarity, axis=1)

# 価格の差分を計算
recommend_candidates['price_diff'] = (recommend_candidates['item_price'] - target_item_price).abs()

# ページ数の差分を計算
recommend_candidates['page_num_diff'] = (recommend_candidates['page_num'] - target_page_num).abs()

# ソート: category_similarity DESC, price_diff ASC, page_num_diff ASC
recommend_candidates_sorted = recommend_candidates.sort_values(
    by=['category_similarity', 'price_diff', 'page_num_diff'],
    ascending=[False, True, True]
)

# 上位3件を取得
top_3_recommendations = recommend_candidates_sorted.head(3)['item_id'].tolist()

# 結果を出力
print(top_3_recommendations)