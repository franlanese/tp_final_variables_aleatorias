import pandas as pd

df = pd.read_csv('steam.csv')

# Crear tabla de frecuencias
tabla = (
    df["required_age"]
    .value_counts()
    .sort_index()
    .reset_index()
)

tabla.columns = ["x (Edad mínima)", "fi"]

# Calcular probabilidades
tabla["p(x) = P(X = x)"] = tabla["fi"] / len(df)

# Agregar columna de frecuencia relativa porcentual
tabla["p(x) = P(X = x) %"] = (tabla["p(x) = P(X = x)"] * 100).round(2)

# Agregar columna de frecuencia acumulada
tabla["Fi"] = tabla["fi"].cumsum()

# Agregar columna de probabilidad acumulada
tabla["P(X ≤ x)"] = tabla["p(x) = P(X = x)"].cumsum().round(6)

# Mostrar tabla con formato bonito
# Versión con estilo para Jupyter (solo columnas necesarias)
tabla_estilo = tabla[['x (Edad mínima)', 'fi', 'p(x) = P(X = x)']].style.background_gradient(cmap='Blues', subset=['p(x) = P(X = x)']).format({
    'fi': '{:,.0f}',
    'p(x) = P(X = x)': '{:.6f}'
})

display(tabla_estilo)