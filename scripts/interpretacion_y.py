import numpy as np
import pandas as pd
from IPython.display import display, Math, Markdown

# 1. Cargar datos y aplicar el mismo filtro que en los pasos anteriores
df = pd.read_csv('steam.csv')
price = df[(df['price'] > 0) & (df['price'] <= 60)]['price']

# 2. Parametros del modelo (mismos que en parametrizacion.py / calculos.py)
n = len(price)
ybar = price.mean()
lam = 1 / ybar
s = price.std(ddof=1)


def FY(y):
    return 1 - np.exp(-lam * y)


# 3. Calcular F_Y(ybar + s)
umbral = ybar + s
prob = FY(umbral)
porcentaje = prob * 100

# --- Resumen de parametros ---
display(Markdown(
    '| Parámetro | Valor |\n'
    '|---|---|\n'
    f'| $\\bar y$ | {ybar:.4f} |\n'
    f'| $s$ | {s:.4f} |\n'
    f'| $\\bar y + s$ | {umbral:.4f} |\n'
    f'| $\\lambda$ | {lam:.4f} |'
))

# --- Calculo de F_Y(ybar + s) ---
display(Math(
    rf'F_Y(\bar y + s) = 1 - e^{{-{lam:.4f}\,({umbral:.4f})}} = {prob:.4f}'
))

display(Markdown(f'Porcentaje esperado por debajo de ($\\bar y + s$): {porcentaje:.2f}%'))
