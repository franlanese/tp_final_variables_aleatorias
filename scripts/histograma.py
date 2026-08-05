import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Cargar datos y aplicar el filtro
df = pd.read_csv('steam.csv')
price = df[(df['price'] > 0) & (df['price'] <= 60)]['price']

# 2. Calcular 'n' y aplicar la Regla de Sturges
n = len(price)
k = int(np.ceil(1 + 3.322 * np.log10(n)))

print(f'Cantidad de datos (n): {n}')
print(f'Intervalos calculados (k): {k}')

# 3. Graficar el histograma de frecuencias relativas (density=True)
plt.figure(figsize=(10, 5))
plt.hist(price, bins=k, density=True, color='skyblue', edgecolor='black')

plt.title(f'Histograma de Frecuencias Relativas (Regla de Sturges: k={k})')
plt.xlabel('Precio (USD)')
plt.ylabel('Frecuencia Relativa / Densidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
