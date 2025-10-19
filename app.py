import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Exploración Dataset de Carros')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Crear dos columnas para los botones
col1, col2 = st.columns(2)

with col1:
    hist_button = st.button('Construir histograma')

with col2:
    scatter_checkbox = st.checkbox('Construir Diagrama de dispersión')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:  # al hacer clic en el botón

    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un scatterplot
    fig = px.scatter(car_data, x="odometer", y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
