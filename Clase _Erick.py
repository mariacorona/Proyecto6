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
fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() # crear gráfico de dispersión