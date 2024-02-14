import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

for i,r in df.iterrows():
   print(r['iso_a3'])
   print(r['currency_code'])
   print(r['local_price'])

print(df.apply(lambda row: row['adj_price'], axis= 1))
print(df.apply(lambda row: row['USD_adjusted'], axis = 1))
