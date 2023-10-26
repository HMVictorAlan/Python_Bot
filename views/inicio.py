from pathlib import Path
from random import randrange
import streamlit as st
from streamlit_tags import st_tags
import openai

from streamlit_option_menu import option_menu
#def load_view():

#def load_view():
import streamlit as st
import pandas as pd


def load_view():

	st.markdown('##')

	# Sección de Introducción
	st.markdown("<h1 style='text-align: center; color: grey'> Bienvenido a Python Bot - Tu Compañero Inteligente de Python </h1>", unsafe_allow_html=True)
	#st.markdown("# Bienvenido a Python Bot - Tu Compañero Inteligente de Python!")
	st.markdown('##')

	col1, col2, col3 = st.columns([.01, .01, .01])
	with col2:
		st.image("assets/images/giphy.gif")
	with col1:
		st.write(' ')
	with col3:
		st.write(' ')

	st.markdown('##')

	st.markdown(
		"Python Bot es una aplicación web dinámica y versátil diseñada para simplificar tus tareas de análisis de datos y programación en Python. Ya seas un científico de datos, analista o alguien que busca aprovechar el poder de Python para la manipulación de datos, esta aplicación es tu solución ideal.")

	# Características Clave
	st.markdown("## Características Clave:")
	st.markdown(
		"- **Análisis de Datos Simplificado**: Sube tus archivos CSV, haz preguntas y recibe análisis de datos perspicaces junto con fragmentos de código en Python.")
	st.markdown(
		"- **Integración de OpenAI**: Hemos integrado el modelo OpenAI GPT-3 para ayudarte a generar código en Python basado en tus consultas, facilitando las tareas de programación complejas. "  " Openai llave: [https://platform.openai.com/](https://platform.openai.com/account/api-keys)")
	st.write()
	st.markdown(
		"- **Personalización**: Adapta tu experiencia con diversas opciones y configuraciones para satisfacer tus necesidades específicas.")

	# Comienza
	st.markdown("## Comienza:")
	st.markdown("Elige una de las siguientes opciones en el menú de navegación:")
	st.markdown("- **Inicio**: Comienza tu viaje de análisis de datos.")
	st.markdown("- **Contacto**: Conoce a la mente detrás de Python Bot.")
	st.markdown(
		"- **Chat**: Comienza a hacer preguntas y desbloquea el poder de la generación de código impulsada por la inteligencia artificial.")
	st.markdown("- **Opciones**: Personaliza tu experiencia con Python Bot.")
	st.markdown("- **Configuración**: Ajusta la configuración y personaliza tus preferencias.")

	st.markdown(
		"¡Estamos emocionados de tenerte a bordo! Si tienes alguna pregunta o necesitas asistencia, no dudes en contactarnos en la sección 'Nosotros'.")
	st.markdown(
		"¡Disfruta usando Python Bot, tu compañero de Python para un análisis de datos y programación más inteligentes!")

# El resto de tu código de Streamlit para la navegación y las vistas va aquí











