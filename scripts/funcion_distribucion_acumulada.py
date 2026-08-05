import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv('steam.csv')

# Tabla de probabilidades acumuladas
tabla = (
    df["required_age"]
    .value_counts()
    .sort_index()
)

Fx = tabla.cumsum() / len(df)

x = Fx.index.tolist()
y = Fx.values.tolist()


# Gráfico F(x) con saltos horizontales
plt.figure(figsize=(8,5))

# Segmentos horizontales
for i in range(len(x)-1):
    plt.hlines(
        y=y[i],
        xmin=x[i],
        xmax=x[i+1],
        linewidth=2
    )

# Último tramo
plt.hlines(
    y=y[-1],
    xmin=x[-1],
    xmax=x[-1]+4,
    linewidth=2
)

# Puntos donde cambia la función
plt.scatter(x, y, s=50)

plt.title("Función de distribución acumulada")
plt.xlabel("Edad mínima requerida (x)")
plt.ylabel("F(x)")

plt.xticks(x)
margen = 0.01

plt.ylim(
    min(y) - margen,
    1 + margen
)
plt.grid(True)

plt.show()