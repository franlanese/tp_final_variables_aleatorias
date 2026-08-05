import pandas as pd

df = pd.read_csv("steam.csv")

valores = sorted(df["required_age"].unique())

print("Valores posibles:")
print([int(x) for x in valores])