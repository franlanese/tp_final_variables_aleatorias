import pandas as pd

df = pd.read_csv("steam.csv")

print("Información general del dataset")
print(f"Cantidad de registros: {len(df)}")
print(f"Cantidad de columnas: {len(df.columns)}")

print("\nPrimeras filas del dataset:")
display(df.head())