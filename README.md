# 🏡 AI Airbnb Finder

Aplicación web que permite buscar alojamientos reales usando Inteligencia Artificial.

## Tecnologías
- Python
- Streamlit
- Gemini CLI
- MCP (Model Context Protocol)
- Airbnb MCP Server

## Cómo funciona
El usuario escribe un destino → la IA consulta Airbnb real → muestra alojamientos con links oficiales.
El sistema usa Gemini CLI como agente autónomo conectado mediante el protocolo MCP al servicio de Airbnb, permitiendo consultar alojamientos reales en tiempo real y mostrarlos en una interfaz interactiva con enlaces oficiales.

## Ejecutar proyecto

1. Clonar repo
2. Crear entorno virtual
3. Instalar dependencias

pip install -r requirements.txt

4. Ejecutar

streamlit run app.py
