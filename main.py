import streamlit as st
import pandas as pd
from langchain.chains import create_sql_query_chain
from pandasai import PandasAI, SmartDataframe
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt
import os

import utils as utl
from views import contacto, options, configuration, inicio

st.set_page_config(layout="wide", page_title='Python Bot')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = utl.get_current_route()
    if route == "inicio":
        inicio.load_view()
    elif route == "contacto":
        contacto.load_view()
    elif route == "chat":

        st.markdown("<h1 style='text-align: center; color: #d4d4d4;'> ¿Qué duda Python tienes? </h1>",
                    unsafe_allow_html=True)
        st.subheader('Sube tu archivo')

        if "last_code_executed" not in st.session_state:
            st.session_state.last_code_executed = None

        if "last_code_generated" not in st.session_state:
            st.session_state.last_code_generated = None

        if "openai_key" not in st.session_state:
            with st.form("Clave API"):
                key = st.text_input("Clave API", value="", type="password")
                if st.form_submit_button("Entregar"):
                    st.session_state.openai_key = key
                    st.session_state.prompt_history = []
                    st.session_state.df = None
                    st.success('Clave API guardada para esta sesión')

        if "openai_key" in st.session_state:
            if st.session_state.df is None:
                uploaded_file = st.file_uploader(
                    "Elija un archivo CSV",
                    type="csv",
                )

                if uploaded_file is not None:
                    df = pd.read_csv(uploaded_file)
                    st.session_state.df = df

            with st.form("Pregunta"):
                question = st.text_input("Pregunta", value="", type="default")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    with st.spinner():
                        llm = OpenAI(api_token=st.session_state.openai_key)
                        pandas_ai = PandasAI(llm)

                        if os.path.isfile('temp_chart.png'):
                            im = plt.imread('temp_chart.png')
                            st.image(im)
                            os.remove('temp_chart.png')

                        executed_code = pandas_ai.run(SmartDataframe(st.session_state.df), prompt=question)
                        if executed_code is not None:
                            st.session_state.last_code_executed = executed_code
                            st.subheader("Resultado:")
                            st.write(executed_code)

                        generated_code = SmartDataframe(st.session_state.df, config={"llm": llm})
                        if generated_code is not None:
                            generated_code.chat(question)
                            st.subheader("Código generado:")
                            st.write(generated_code.last_code_generated)

                   # st.session_state.prompt_history.append(question)

            if st.session_state.df is not None:
                st.subheader("Marco de datos actual:")
                st.write(st.session_state.df)

        if st.button("Borrar"):
            st.session_state.prompt_history = []
            st.session_state.df = None

    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route is None:
        inicio.load_view()


# Call the navigation function
navigation()
