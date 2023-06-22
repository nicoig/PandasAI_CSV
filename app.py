# PandasAI con Streamlit

# Para crear el requirements.txt ejecutamos 
# pipreqs --encoding=utf8

# Instalando librerías
# pip install pandasai streamlit emoji python-dotenv

import streamlit as st 
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# El emoji de rayo en Unicode es \U000026A1
st.title("\U000026A1 BitBoosters \U000026A1")
st.subheader("Crea Gráficos al instante")

uploaded_file = st.file_uploader("Carga tu archivo", type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8', delimiter=',')
        st.write(df.head(3))

        # Cargar la clave de API desde la variable de entorno
        api = os.getenv("OPENAI_API_KEY")

        # Crear un LLM instanciando el objeto OpenAI y pasando el token de la API
        llm = OpenAI(api_token=api)

        # Crear objeto PandasAI, pasando el LLM y ajustando la opción conversacional en Falso
        pandas_ai = PandasAI(llm, conversational=False)

        # Input text for the user's prompt
        prompt = st.text_area("Ingresa tu solicitud:")

        # Generar salida usando el agente definido en la solicitud
        if st.button("Generar"):
            if prompt:
                # Llamar a pandas_ai.run(), pasando dataframe y prompt
                with st.spinner("Generando respuesta..."):
                    result = pandas_ai.run(df, prompt)

                    # Comprueba el tipo de objeto devuelto
                    if isinstance(result, pd.DataFrame):
                        # Si es un DataFrame, escríbelo en Streamlit
                        st.write(result)
                    else:
                        # Para otros tipos de salida, simplemente escribe el resultado en Streamlit
                        st.write(result)
            else:
                st.warning("Por favor, ingresa una solicitud.")

                
    except pd.errors.EmptyDataError:
        st.error("El archivo CSV está vacío. Por favor, carga un archivo CSV válido.")
    except pd.errors.ParserError:
        st.error("Ocurrió un error al analizar el archivo CSV. Verifica que el archivo esté en el formato correcto.")
    except Exception as e:
        st.error(f"Ocurrió un error desconocido al leer el archivo: {e}")


# Actualizar Repo de Github
# git add .
# git commit -m "Se actualizan las variables de entorno"
# git push origin master

