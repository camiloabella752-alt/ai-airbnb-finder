import streamlit as st
from gemini_client import buscar_airbnb

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# ---- HEADER ----
st.markdown("""
<h1 style='text-align: center;'>🌍 Planificador de Viajes con IA</h1>
<p style='text-align: center;'>Busca alojamientos usando Inteligencia Artificial</p>
<hr>
""", unsafe_allow_html=True)

# ---- FORMULARIO ----
col1, col2, col3 = st.columns(3)

with col1:
    destino = st.text_input("📍 Destino", placeholder="Ej: Bogotà")

with col2:
    fechas = st.text_input("📅 Fechas", placeholder="Ej: 10 - 15 Marzo")

with col3:
    personas = st.number_input("👥 Personas", min_value=1, value=2)

buscar = st.button("🔍 Buscar alojamiento", use_container_width=True)


# ---- RESULTADOS ----
if buscar and destino:

    with st.spinner("Consultando alojamientos..."):
        resultados = buscar_airbnb(destino, fechas, personas)

    if resultados:

        st.success("Opciones encontradas ✨")

        cols = st.columns(3)

        for i, lugar in enumerate(resultados):
            with cols[i % 3]:

                st.markdown(f"""
                ### 🏡 {lugar.get('nombre','Alojamiento')}
                📍 {lugar.get('ubicacion','')}
                
                ⭐ {lugar.get('rating','')}
                
                💲 {lugar.get('precio','')}
                
                {lugar.get('descripcion','')}
                """)

                url = lugar.get("url", "")
                if url:
                    st.link_button("🔗 Ver en Airbnb", url, use_container_width=True)

                st.divider()

    else:
        st.error("No se pudieron obtener resultados")

