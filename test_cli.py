import subprocess

def preguntar_a_gemini(texto):
    proceso = subprocess.run(
        ["gemini", texto],
        capture_output=True,
        text=True
    )
    return proceso.stdout

print(preguntar_a_gemini("hola"))
