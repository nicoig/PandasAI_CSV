# PandasAI con Streamlit

# Para crear el requirements.txt ejecutamos 
# pipreqs --encoding=utf8 --force

# Instalando librerías
# pip install pandasai streamlit emoji python-dotenv
# pip freeze | findstr matplotlib >> requirements.txt


import streamlit as st 
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import os
from dotenv import load_dotenv
import matplotlib
import matplotlib.pyplot as plt
import csv
#import tkinter as tk

#matplotlib.use('TkAgg')

load_dotenv()

st.title("\U000026A1 BitBoosters \U000026A1")
st.markdown("<p style='color: white; font-size: 15px;'>Carga tus archivos Excel o CSV, realiza consultas en lenguaje natural, crea gráficos de manera intuitiva y descubre los insights que tus datos tienen para ofrecerte.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Carga tu archivo", type=['csv', 'xlsx'])

if uploaded_file is not None:
    df = None
    if uploaded_file is not None:
        df = None
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.type == "text/csv":
            preview = uploaded_file.read(1024).decode()  # Lee los primeros 1024 bytes del archivo
            dialect = csv.Sniffer().sniff(preview)
            uploaded_file.seek(0)  # Regresa al inicio del archivo después de la previsualización
            df = pd.read_csv(uploaded_file, encoding='utf-8', delimiter=dialect.delimiter)
        else:
            st.error("El tipo de archivo no es compatible. Por favor, carga un archivo CSV o Excel.")


    if df is not None:
        st.write(df.head(4))

        api = os.getenv("OPENAI_API_KEY")
        llm = OpenAI(api_token=api)
        pandas_ai = PandasAI(llm, conversational=False)

        prompt = st.text_area("Ingresa tu solicitud:")
        if st.button("Generar"):
            if prompt:
                with st.spinner("Generando respuesta..."):
                    result = pandas_ai.run(df, prompt)
                    fig_number = plt.get_fignums()
                    if fig_number:
                        st.pyplot(plt.gcf())
                    elif isinstance(result, pd.DataFrame):
                        st.write(result)
                    else:
                        st.write(result)
            else:
                st.warning("Por favor, ingresa una solicitud.")



# Actualizar Repo de Github
# git add .
# git commit -m "Se actualizan las variables de entorno"
# git push origin master

# En Render
# agregar en variables de entorno
# PYTHON_VERSION = 3.9.12