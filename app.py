
import pandas as pd
import streamlit as st 
import plotly.express as px 

disp_boton = st.button("Construir gráfico de dispersión")

if disp_boton :
      
    st.write("Creacion de un gráfico de dispersión")
      
    fig_disp = px.scatter(datos, x="odometer", y="price") # crear un gráfico de dispersión
      
    st.plotly_chart(fig_disp) # crear gráfico de dispersión
    