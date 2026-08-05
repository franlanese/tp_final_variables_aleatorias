import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('steam.csv')

df = df[df["required_age"] > 0]

tabla = (
    df["required_age"]
    .value_counts()
    .sort_index()
    .reset_index()
)

tabla.columns = ["x", "fi"]

tabla["pX(x)"] = tabla["fi"] / len(df)

plt.figure(figsize=(12,6))

plt.bar(
    tabla["x"].astype(str),
    tabla["pX(x)"]
)

plt.title("Función de probabilidad puntual - Edad requerida")
plt.xlabel("Edad requerida")
plt.ylabel("P(X=x)")

plt.grid(axis="y", alpha=0.3)

plt.show()