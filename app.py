import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
df = pd.read_csv("vehicles_us.csv")

# Encabezado principal
st.header("Análisis de vehículos en venta")

# Mostrar los primeros datos
st.write("Vista previa de los datos:")
st.write(df.head())

# Histograma (casilla de verificación)
if st.checkbox("Mostrar histograma del odómetro"):
    st.write("Histograma del kilometraje")
    fig = px.histogram(df, x="odometer", title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Dispersión (casilla de verificación)
if st.checkbox("Mostrar dispersión Precio vs Año"):
    st.write("Relación entre precio y año del modelo")
    fig2 = px.scatter(df, x="model_year", y="price", title="Precio vs Año del modelo")
    st.plotly_chart(fig2, use_container_width=True)