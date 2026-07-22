import pandas as pd

pd.set_option('display.max_columns', 15)
df = pd.read_csv('steam.csv')

print(df.head())

print(df.info())