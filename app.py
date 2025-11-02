import streamlit as st

# =========================================================
# FUNCIÓN ECA AGUA
# =========================================================
def verificar_eca_agua():
    st.header("💧 Evaluación del ECA - Agua (D.S. N° 004-2017-MINAM)")
    categoria = st.selectbox("Seleccione la categoría:", [
        "1. Poblacional y recreacional",
        "2. Actividades marino–costeras/continentales",
        "3. Riego y bebida de animales",
        "4. Conservación del ambiente acuático"
    ])

    # Diccionarios de límites según categoría
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

    if st.button("Evaluar ECA Agua"):
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

    if st.button("Evaluar ECA Aire"):
        limite = limites[contaminante][periodo]
        if valor <= limite:
            st.success(f"✅ Cumple con el ECA-Aire ({valor} ≤ {limite})")
        else:
            st.error(f"🚫 No cumple con el ECA-Aire ({valor} > {limite})")


# =========================================================
# INTERFAZ PRINCIPAL
# =========================================================
st.title("🌎 Sistema Integral de Monitoreo Ambiental")

opcion = st.sidebar.radio("Seleccione módulo:", ["ECA Agua", "ECA Aire"])

if opcion == "ECA Agua":
    verificar_eca_agua()
elif opcion == "ECA Aire":
    verificar_eca_aire()
