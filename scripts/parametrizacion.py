import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Math

# 1. Cargar datos y aplicar el mismo filtro que en sturges.py
df = pd.read_csv('steam.csv')
price = df[(df['price'] > 0) & (df['price'] <= 60)]['price']

# 2. Calcular la media muestral y estimar lambda (método de los momentos)
n = len(price)
ybar = price.mean()
lam = 1 / ybar

display(Math(rf'\bar y = \frac{{\sum y_i}}{{n}} = \frac{{{price.sum():.2f}}}{{{n}}} = {ybar:.4f}'))
print(f'Media muestral: {ybar:.4f}')
print('\n')

display(Math(rf'\lambda = \frac{{1}}{{\bar y}} = \frac{{1}}{{{ybar:.4f}}} = {lam:.4f}'))

print(f'Lambda estimado: {lam:.4f}')
print('\n')

# 3. Reemplazar lambda en el modelo teorico general para obtener la curva especifica
display(Math(rf'f_Y(y) = {lam:.4f}\,e^{{-{lam:.4f}\,y}}, \quad y \ge 0'))

# 4. Graficar el histograma real junto con la curva teorica ajustada
k = int(np.ceil(1 + 3.322 * np.log10(n)))

plt.figure(figsize=(10, 5))
plt.hist(price, bins=k, density=True, color='skyblue', edgecolor='black', label='Histograma (datos reales)')

y_vals = np.linspace(0, price.max(), 500)
f_vals = lam * np.exp(-lam * y_vals)
plt.plot(y_vals, f_vals, color='red', linewidth=2, label=f'Curva de densidad (λ={lam:.4f})')

plt.title('Histograma de Precios vs. Curva de densidad (Exponencial)')
plt.xlabel('Precio (USD)')
plt.ylabel('Densidad')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
