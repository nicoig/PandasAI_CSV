'''

# PandasAI con Streamlit

# Instalando librerías
# pip install pandasai streamlit

import streamlit as st 
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

st.title("BitBoosters - Crea gráficos al instante")

uploaded_file = st.file_uploader("Carga tu archivo", type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8', delimiter=',')
        st.write(df.head(3))
        
        # nuevo código a continuación...
        prompt = st.text_area("Ingresa tu solicitud:")

        # Crear un LLM instanciando el objeto OpenAI y pasando el token de la API
        llm = OpenAI(api_token="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")

        # Crear objeto PandasAI, pasando el LLM
        pandas_ai = PandasAI(llm)

        # Generar salida
        if st.button("Generar"):
            if prompt:
                # Llamar a pandas_ai.run(), pasando dataframe y prompt
                with st.spinner("Generando respuesta..."):
                    st.write(pandas_ai.run(df, prompt))
            else:
                st.warning("Por favor, ingresa una solicitud.")
    except pd.errors.EmptyDataError:
        st.error("El archivo CSV está vacío. Por favor, carga un archivo CSV válido.")
    except pd.errors.ParserError:
        st.error("Ocurrió un error al analizar el archivo CSV. Verifica que el archivo esté en el formato correcto.")
    except Exception as e:
        st.error(f"Ocurrió un error desconocido al leer el archivo: {e}")


'''

# PandasAI con Streamlit}

# Para crear el requirements.txt ejecutamos 
# pipreqs --encoding=utf8

# Instalando librerías
# pip install pandasai streamlit emoji

import streamlit as st 
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib.figure


# El emoji de rayo en Unicode es \U000026A1
st.title("\U000026A1 BitBoosters \U000026A1")

uploaded_file = st.file_uploader("Carga tu archivo", type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8', delimiter=',')
        st.write(df.head(3))

        # Crear un LLM instanciando el objeto OpenAI y pasando el token de la API
        llm = OpenAI(api_token="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")

        # Crear objeto PandasAI, pasando el LLM y ajustando la opción conversacional en Falso
        pandas_ai = PandasAI(llm, conversational=False)

        # Input text for the user's prompt
        prompt = st.text_area("Ingresa tu solicitud:")

        # Generar salida usando el agente definido en la solicitud
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
                    elif isinstance(result, matplotlib.figure.Figure):
                        # Si es una figura de matplotlib, dibújala en Streamlit
                        st.pyplot(result)
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

