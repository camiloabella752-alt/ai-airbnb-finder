import subprocess
import json
import re


def extraer_json(texto):
    try:
        match = re.search(r"\[.*\]", texto, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    except:
        pass
    return []


def buscar_airbnb(destino, fechas, personas):

   
    prompt = f"""
Use the airbnb_search tool to find stays.

location: {destino}
dates: {fechas}
guests: {personas}

Return ONLY a valid JSON array like:

[
  {{
    "nombre": "",
    "precio": "",
    "rating": "",
    "ubicacion": "",
    "descripcion": "",
    "url": ""
  }}
]

The url must be the official Airbnb listing link.
"""


    proceso = subprocess.run(
        ["gemini", "--yolo", "-p", prompt],
        capture_output=True,
        text=True
    )

    respuesta = proceso.stdout
    return extraer_json(respuesta)
