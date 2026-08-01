import numpy as np
import pandas as pd
from IPython.display import display, Math

# 1. Cargar datos y aplicar el mismo filtro que en los pasos anteriores
df = pd.read_csv('steam.csv')
price = df[(df['price'] > 0) & (df['price'] <= 60)]['price']

# 2. Parametros del modelo (mismos que en parametrizacion.py)
n = len(price)
ybar = price.mean()
lam = 1 / ybar
s = price.std(ddof=1)  # desviacion estandar muestral


def FY(y):
    return 1 - np.exp(-lam * y)


# 3. Verificacion de normalizacion: F_Y evaluada en un valor muy grande
#    equivale a integrar f_Y(y) entre 0 e infinito
area = FY(1e6)

# 4. Probabilidades concretas
p_menor_ybar = FY(ybar)
p_mayor_ybar_mas_s = 1 - FY(ybar + s)

print(f'n: {n}')
print(f'Media muestral (y_barra): {ybar:.4f}')
print(f'Desvio estandar muestral (s): {s:.4f}')
print(f'Lambda: {lam:.4f}')
print(f'Area bajo f_Y(y) entre 0 e infinito (aprox): {area:.6f}')
print(f'P(Y <= y_barra) = {p_menor_ybar:.4f}')
print(f'P(Y > y_barra + s) = {p_mayor_ybar_mas_s:.4f}')

display(Math(rf'\int_0^\infty f_Y(y)\,dy = F_Y(\infty) - F_Y(0) = {area:.4f} \approx 1'))
display(Math(rf'F_Y(y) = 1 - e^{{-{lam:.4f}\,y}}'))
display(Math(rf'P(Y \le \bar y) = F_Y({ybar:.4f}) = {p_menor_ybar:.4f}'))
display(Math(rf'P(Y > \bar y + s) = 1 - F_Y({ybar:.4f} + {s:.4f}) = {p_mayor_ybar_mas_s:.4f}'))
