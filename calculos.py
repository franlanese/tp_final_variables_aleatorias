import numpy as np
import pandas as pd
from IPython.display import display, Math, Markdown

# 1. Cargar datos y aplicar el mismo filtro que en los pasos anteriores
df = pd.read_csv('steam.csv')
price = df[(df['price'] > 0) & (df['price'] <= 60)]['price']

# 2. Parametros del modelo (mismos que en parametrizacion.py)
n = len(price)
ybar = price.mean()
lam = 1 / ybar
suma_desvios_cuad = ((price - ybar) ** 2).sum()  # suma de (y_i - ybar)^2
s = price.std(ddof=1)  # desviacion estandar muestral


def FY(y):
    return 1 - np.exp(-lam * y)


# 3. Verificacion de normalizacion: F_Y evaluada en un valor muy grande
#    equivale a integrar f_Y(y) entre 0 e infinito
area = FY(1e6)

# 4. Probabilidades concretas
p_menor_ybar = FY(ybar)
p_mayor_ybar_mas_s = 1 - FY(ybar + s)

# --- Desviacion estandar muestral ---
display(Math(
    rf's = \sqrt{{\dfrac{{1}}{{n-1}}\sum_{{i=1}}^{{n}}(y_i-\bar y)^2}} '
    rf'= \sqrt{{\dfrac{{{suma_desvios_cuad:.2f}}}{{{n - 1}}}}} = {s:.4f}'
))

# --- Resumen de parametros ---
display(Markdown(
    '| Parámetro | Valor |\n'
    '|---|---|\n'
    f'| n | {n} |\n'
    f'| Media muestral ($\\bar y$) | {ybar:.4f} |\n'
    f'| Desvío estándar muestral ($s$) | {s:.4f} |\n'
    f'| Tasa ($\\lambda$) | {lam:.4f} |'
))

# --- Probabilidades concretas ---
display(Math(rf'P(Y \le \bar y) = F_Y({ybar:.4f}) = {p_menor_ybar:.4f}'))
display(Math(rf'P(Y > \bar y + s) = 1 - F_Y({ybar:.4f} + {s:.4f}) = {p_mayor_ybar_mas_s:.4f}'))
