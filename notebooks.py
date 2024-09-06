import pandas as pd
import streamlit as st 
import plotly.express as px 

datos= pd.read_csv('vehicles_us.csv')

#print(datos.head())

hist_boton = st.button("Construir histograma")

if hist_boton :
      
    st.write("Creacion de un histograma de los valores del odometro de los autos")
      
    fig = px.histogram(datos, x= "odometer")
      
    st.plotly_chart(fig)
      


car_data = pd.read_csv('vehicles_us.csv') # leer los datos

disp_boton = st.button("Construir gráfico de dispersión")

if disp_boton :
      
    st.write("Creacion de un gráfico de dispersión")
      
    fig_disp = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
      
    st.plotly_chart(fig_disp) # crear gráfico de dispersión
    