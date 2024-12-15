#csvファイルを読み込み
import pandas as pd
df = pd.read_csv('winequality-red.csv')

#”quality”の値ごとにカテゴリーごとの平均を表示する
quality_means = df.groupby('quality').mean()
print(quality_means)