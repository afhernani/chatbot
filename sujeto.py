# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def extraer_tecnologia():
    url = "https://sujeto.es/50-preguntas-sobre-tecnologia-con-respuestas/"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("Error al acceder a la página:", r.status_code)
        return

    soup = BeautifulSoup(r.text, "html.parser")

    preguntas_respuestas = []

    for p in soup.find_all("p"):
        texto = p.get_text().strip()
        if not texto:
            continue

        # Relajamos un poco el filtro
        if texto.startswith("¿"):
            preguntas_respuestas.append(texto)
        elif len(preguntas_respuestas) % 2 == 1:
            preguntas_respuestas.append(texto)

    if not preguntas_respuestas:
        print("No se encontraron preguntas ni respuestas. Revisa la estructura del HTML.")
    else:
        with open("faq_tecnologia_subj.txt", "w", encoding="utf-8") as f:
            for linea in preguntas_respuestas:
                f.write(linea + "\n")

extraer_tecnologia()
