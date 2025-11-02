import streamlit as st

# =========================================================
# CONFIGURACIÓN INICIAL
# =========================================================
st.set_page_config(
    page_title="Sistema Integral de Monitoreo Ambiental",
    page_icon="🌎",
    layout="centered",
)

# Encabezado con imagen y título
st.image("https://thumbs.dreamstime.com/z/icono-de-reconocimiento-marino-para-el-monitoreo-ambiental-y-dise%C3%B1o-vectores-recolecci%C3%B3n-datos-ia-generativa-un-vectorial-389255579.jpg?ct=jpeg", width=True)
st.title("🌎 Sistema Integral de Monitoreo Ambiental")
st.markdown("---")

st.markdown("""
Bienvenido al **Sistema Integral de Monitoreo Ambiental**, una herramienta interactiva para evaluar el
cumplimiento de los **Estándares de Calidad Ambiental (ECA)** del aire y del agua conforme a la normativa peruana del **MINAM**.
""")

# =========================================================
# FUNCIÓN ECA AGUA
# =========================================================
def verificar_eca_agua():
    st.header("💧 Evaluación del ECA - Agua (D.S. N° 004-2017-MINAM)")
    st.image("https://i.pinimg.com/236x/d2/b2/af/d2b2afbb7953436c9cdc7637be722464.jpg", width=500)
    
    categoria = st.selectbox("Seleccione la categoría:", [
        "1. Poblacional y recreacional",
        "2. Actividades marino–costeras/continentales",
        "3. Riego y bebida de animales",
        "4. Conservación del ambiente acuático"
    ])
    
    limites_categorias = {
        "1": {
            "A1": {"pH_min": 6.5, "pH_max": 8.5, "DBO": 3, "DQO": 10, "Arsénico": 0.01, "Cromo total": 0.05},
            "A2": {"pH_min": 6.5, "pH_max": 9.0, "DBO": 5, "DQO": 20, "Arsénico": 0.01, "Cromo total": 0.05},
            "A3": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 10, "DQO": 30, "Arsénico": 0.05, "Cromo total": 0.1},
            "B1": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 5, "DQO": 25, "Arsénico": 0.05, "Cromo total": 0.1},
            "B2": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 10, "DQO": 40, "Arsénico": 0.1, "Cromo total": 0.1}
        },
        "2": {
            "C1": {"pH_min": 6.5, "pH_max": 8.5, "DBO": 3, "DQO": 10, "Arsénico": 0.01, "Cromo total": 0.05},
            "C2": {"pH_min": 6.5, "pH_max": 9.0, "DBO": 5, "DQO": 20, "Arsénico": 0.05, "Cromo total": 0.1},
            "C3": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 10, "DQO": 30, "Arsénico": 0.1, "Cromo total": 0.1},
            "C4": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 15, "DQO": 40, "Arsénico": 0.2, "Cromo total": 0.2}
        },
        "3": {
            "D1": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 10, "DQO": 25, "Arsénico": 0.05, "Cromo total": 0.1},
            "D2": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 15, "DQO": 40, "Arsénico": 0.1, "Cromo total": 0.2}
        },
        "4": {
            "E1": {"pH_min": 6.5, "pH_max": 8.5, "DBO": 5, "DQO": 15, "Arsénico": 0.01, "Cromo total": 0.05},
            "E2": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 8, "DQO": 25, "Arsénico": 0.05, "Cromo total": 0.1},
            "E3": {"pH_min": 6.0, "pH_max": 9.0, "DBO": 10, "DQO": 35, "Arsénico": 0.1, "Cromo total": 0.1}
        }
    }

    cat_key = categoria.split(".")[0]
    subcat = st.selectbox("Seleccione subcategoría:", list(limites_categorias[cat_key].keys()))
    limites = limites_categorias[cat_key][subcat]

    st.subheader("Ingrese los valores medidos:")
    ph = st.number_input("pH", min_value=0.0, step=0.1)
    dbo = st.number_input("DBO (mg/L)", min_value=0.0, step=0.1)
    dqo = st.number_input("DQO (mg/L)", min_value=0.0, step=0.1)
    arsenico = st.number_input("Arsénico (mg/L)", min_value=0.0, step=0.001)
    cromo = st.number_input("Cromo total (mg/L)", min_value=0.0, step=0.001)

    if st.button("Evaluar ECA Agua 💧"):
        resultados = {
            "pH": limites["pH_min"] <= ph <= limites["pH_max"],
            "DBO": dbo <= limites["DBO"],
            "DQO": dqo <= limites["DQO"],
            "Arsénico": arsenico <= limites["Arsénico"],
            "Cromo total": cromo <= limites["Cromo total"]
        }

        st.subheader("📊 Resultados:")
        for k, v in resultados.items():
            if v:
                st.success(f"✅ {k} cumple con el ECA")
            else:
                st.error(f"🚫 {k} excede el límite permitido")

        if all(resultados.values()):
            st.success("🌿 El agua cumple totalmente con el ECA establecido.")
        else:
            st.warning("⚠️ El agua no cumple completamente con el ECA.")


# =========================================================
# FUNCIÓN ECA AIRE
# =========================================================
def verificar_eca_aire():
    st.header("🌬️ Evaluación del ECA - Aire (D.S. N° 003-2017-MINAM)")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5nra3jS4p3oxm0f-PANCmgeweIlVOJ6bqCw&s", width=500)

    limites = {
        "SO2": {"24h": 250},
        "NO2": {"1h": 200, "anual": 100},
        "PM2.5": {"24h": 50, "anual": 25},
        "PM10": {"24h": 100, "anual": 50},
        "CO": {"1h": 30000, "8h": 10000},
        "O3": {"8h": 100},
        "Pb": {"mensual": 1.5, "anual": 0.5},
        "Benceno": {"anual": 2},
        "H2S": {"24h": 150},
        "Hg": {"24h": 2}
    }

    contaminante = st.selectbox("Seleccione contaminante:", list(limites.keys()))
    periodo = st.selectbox("Periodo de medición:", list(limites[contaminante].keys()))
    valor = st.number_input(f"Ingrese valor medido ({periodo}) en µg/m³", min_value=0.0)

    if st.button("Evaluar ECA Aire 🌬️"):
        limite = limites[contaminante][periodo]
        if valor <= limite:
            st.success(f"✅ Cumple con el ECA-Aire ({valor} ≤ {limite})")
        else:
            st.error(f"🚫 No cumple con el ECA-Aire ({valor} > {limite})")


# =========================================================
# INTERFAZ PRINCIPAL
# =========================================================
opcion = st.sidebar.radio("Seleccione módulo:", ["🏞️ ECA Agua", "🌆 ECA Aire", "📘 Créditos"])

if opcion == "🏞️ ECA Agua":
    verificar_eca_agua()
elif opcion == "🌆 ECA Aire":
    verificar_eca_aire()
else:
    st.header("📘 Créditos")
    #st.image("https://cdn.pixabay.com/photo/2017/02/15/12/12/code-2065930_1280.jpg", width=500)
    st.markdown("""
    **Curso:** Técnicas de Programación I  
    💻 Desarrollado con [Streamlit](https://streamlit.io)  
    🌎 Proyecto de aprendizaje interactivo sobre estándares ambientales.
    """)

st.markdown("---")
st.caption("© 2025 Sistema Integral de Monitoreo Ambiental - MINAM (Demo educativa)")
