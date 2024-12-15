#csvファイルを読み込み
import pandas as pd
df = pd.read_csv('winequality-red.csv')

#”quality”が6以上のデータを”quality”の高い順で表示する
quality_six_or_more = df[df['quality'] >= 6]
quality_six_or_more_sorted = quality_six_or_more.sort_values(by='quality', ascending=False)
print(quality_six_or_more_sorted)