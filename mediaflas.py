# -*- coding: utf-8 -*-
from flask import Flask, send_from_directory
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

FILE_NAME = "faq_tecnologia_subj.txt"

def extraer_tecnologia():
    url = "https://sujeto.es/50-preguntas-sobre-tecnologia-con-respuestas/"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    preguntas_respuestas = []
    for p in soup.find_all("p"):
        texto = p.get_text().strip()
        if not texto:
            continue
        if texto.startswith("¿"):
            preguntas_respuestas.append(texto)
        elif len(preguntas_respuestas) % 2 == 1:
            preguntas_respuestas.append(texto)

    # Guardar en archivo
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for linea in preguntas_respuestas:
            f.write(linea + "\n")

@app.route("/")
def index():
    return """<html>
    <body>
        <h1>Descargar FAQ Tecnológico</h1>
        <a href="/download">Descargar archivo FAQ</a>
    </body>
    </html>"""

@app.route("/download")
def download():
    # Asegurar que el archivo está generado
    if not os.path.exists(FILE_NAME):
        extraer_tecnologia()
    return send_from_directory(directory=os.getcwd(), path=FILE_NAME, as_attachment=True)

if __name__ == "__main__":
    extraer_tecnologia()
    app.run(host="0.0.0.0", port=5000, debug=True)
