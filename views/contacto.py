import streamlit as st
from PIL import Image


def load_view():
    Descripción = """
    Analista de Datos con sólidos conocimientos de matemáticas, física, estadística y programación, necesarios para proponer soluciones a problemas complejos de ingeniería. 
    Extraer y limpiar información/datos analizados y visualizados dentro de "historias" en los datos es lo que uso para comunicar soluciones.

    Espero desarrollar mi carrera en Análisis de Datos y Inteligencia de Negocios mientras crece tanto personal como profesionalmente.
    """
    correo = "hmvictoralan@gmail.com"
    MEDIOS_DE_COMUNICACIÓN_SOCIAL = {
        "Discord": "",
        "LinkedIn": "https://www.linkedin.com/in/victoralan-hernandezmunoz/",
        "GitHub": "https://github.com",
        "Twitter": "https://twitter.com",
    }

    st.markdown("<h1 style='text-align: center; color: grey'>  </h1>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/images/profile_pic.png", width=333)
    with col2:
        st.markdown("<h1 style='text-align: center; color: grey'> Victor Alan Hernandez Muñoz </h1>",
                    unsafe_allow_html=True)
        st.markdown('##')
        st.write(Descripción)
        st.write("📫", correo)
        # st.download_button(
        # label=" 📄 Download Resume",
        # data=PDFbyte,
        # file_name=resume_file.name,
        # mime="application/octet-stream",)

    # --- VÍNCULOS SOCIALES ---
    st.write('\n')
    cols = st.columns(len(MEDIOS_DE_COMUNICACIÓN_SOCIAL))
    for index, (platform, link) in enumerate(MEDIOS_DE_COMUNICACIÓN_SOCIAL.items()):
        cols[index].write(f"[{platform}]({link})")

    # --- Calificaciones
    st.write('\n')
    st.subheader("Calificaciones")
    st.write(
        """
    - ✔️ SQL CON MYSQL: Instalando y configurando MySQL, Manipulando la base de datos, Administrando las tablas de la base de datos, Mantenimiento de los datos en las tablas, Consultando los datos.
    - ✔️ JAVA Y JPA: CONSULTAS AVANZADAS, RENDIMIENTO Y MODELOS COMPLEJOS: Criteria API
    - ✔️ JAVA POLIMORFISMO: ENTENDIENDO HERENCIA E INTERFACES: Introducción a herencia, Super y reescrita de Métodos, Entendiendo Polimorfismo, Herencia y el uso de constructores, Practicando herencia e interfaces
    - ✔️ GIT Y GITHUB: CONTROLE Y COMPARTA SU CÓDIGO: Iniciando los trabajos, Compartiendo el trabajo, Trabajando en equipo, Manipulando las versiones, Generando entregas
    """
    )

    # --- HABILIDADES ---
    st.write('\n')
    st.subheader("Habilidades")
    st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, JAVA, JDBC, JPA, Selenium, Streamlit, Google Tag Manager Fundamentals
    - 📊 Data Visulization: Tableau, MS Excel, Streamlit, Presentation Skills
    - 📚 Modeling: Logistic regression, linear regression, Regression Testing, Random Forest, Docker Products
    - 🗄️ Databases: Postgres, MongoDB, MySQL, SQLite
    """
    )
















