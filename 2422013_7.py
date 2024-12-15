
#csvファイルを読み込み
import pandas as pd
df = pd.read_csv('winequality-red.csv')

#csvファイルの5行目から10行目のみを表示
print(df.iloc[4:10])