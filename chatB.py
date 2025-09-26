# -*- coding: utf-8 -*-
# pip install nltk scikit-learn pymongo requests

import tkinter as tk
from tkinter import scrolledtext
import nltk
import random
import string
import csv
import requests
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Inicialización NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.corpus import stopwords
spanish_stopwords = stopwords.words('spanish')

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["chatmemory"]
memoria = db["conversaciones"]
aprendizaje = db["aprendizaje"]

# Recuperar historial previo
historial_conversacion = list(memoria.find({}, {"_id": 0}))

# Cargar corpus
with open('chatbot.txt', 'r', errors='ignore', encoding='utf-8') as f:
    raw = f.read().lower()
sent_tokens = nltk.sent_tokenize(raw, language='spanish')
for turno in historial_conversacion:
    sent_tokens.append(turno["robo"])

# Preprocesamiento
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens): return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(p), None) for p in string.punctuation)
def LemNormalize(text): return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict), language='spanish'))

# Saludos
GREETING_INPUTS = ("hola", "buenas", "saludos", "qué tal", "hey")
GREETING_RESPONSES = ["¡Hola!", "¡Hey!", "*asiente*", "Hola, ¿qué tal?", "¡Encantado de hablar contigo!"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# APIs externas
def consulta_wikipedia(pregunta):
    url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{pregunta.replace(' ', '_')}"
    try:
        r = requests.get(url)
        data = r.json()
        if 'extract' in data:
            return data['extract']
    except:
        return None

def consulta_clima(ciudad):
    clave = "TU_API_KEY_OPENWEATHER"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave}&units=metric&lang=es"
    try:
        r = requests.get(url)
        data = r.json()
        if data.get("main"):
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"En {ciudad} hay {desc} con {temp}°C."
    except:
        return None

def consulta_curiosidad(fecha):
    url = f"http://numbersapi.com/{fecha}/date?json"
    try:
        r = requests.get(url)
        data = r.json()
        return data.get("text")
    except:
        return None

def consulta_noticias():
    clave = "TU_API_KEY_NEWSAPI"
    url = f"https://newsapi.org/v2/top-headlines?country=es&category=general&apiKey={clave}"
    try:
        r = requests.get(url)
        data = r.json()
        if data.get("articles"):
            return data["articles"][0]["title"]
    except:
        return None

# Modo explorador
modo_explorador = False
def activar_explorador():
    global modo_explorador
    modo_explorador = not modo_explorador
    estado = "activado" if modo_explorador else "desactivado"
    chat_window.insert(tk.END, f"ROBO: Modo explorador {estado}.\n")

def sugerir_tema():
    temas = [
        "¿Sabías que el cerebro humano consume el 20% de la energía del cuerpo?",
        "¿Quieres saber qué pasó un día como hoy en la historia?",
        "¿Te interesa conocer una curiosidad científica?",
        "¿Te cuento una noticia cultural actual?",
        "¿Te gustaría saber algo sobre salud preventiva?"
    ]
    return random.choice(temas)

# Generar respuesta
def response(user_response):
    resultado = aprendizaje.find_one({"pregunta": {"$regex": user_response, "$options": "i"}})
    if resultado and resultado["respuesta"]:
        return resultado["respuesta"]

    for turno in reversed(historial_conversacion):
        if user_response.lower() in turno["usuario"].lower():
            return turno["robo"]

    respuesta_api = consulta_wikipedia(user_response)
    if respuesta_api:
        return respuesta_api

    if "clima" in user_response or "tiempo" in user_response:
        ciudad = user_response.split()[-1]
        clima = consulta_clima(ciudad)
        if clima:
            return clima

    if "fecha" in user_response or "día" in user_response:
        curiosidad = consulta_curiosidad("9/20")
        if curiosidad:
            return curiosidad

    robo_response = ''
    temp_tokens = sent_tokens.copy()
    temp_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=spanish_stopwords)
    tfidf = TfidfVec.fit_transform(temp_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        aprendizaje.insert_one({"pregunta": user_response, "respuesta": None})
        sugerencia = temp_tokens[idx] if idx < len(temp_tokens) else None
        return f"No estoy seguro, pero quizás te refieres a:\n→ {sugerencia}\nLo guardaré para aprender más adelante."
    else:
        return temp_tokens[idx]

# Enviar mensaje
def send(event=None):
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_window.insert(tk.END, "Tú: " + user_input + "\n")
    entry.delete(0, tk.END)

    if modo_explorador:
        propuesta = sugerir_tema()
        chat_window.insert(tk.END, f"ROBO: {propuesta}\n")
        if "noticia" in propuesta:
            noticia = consulta_noticias()
            if noticia:
                chat_window.insert(tk.END, f"ROBO: {noticia}\n")
        elif "historia" in propuesta:
            historia = consulta_curiosidad("9/20")
            if historia:
                chat_window.insert(tk.END, f"ROBO: {historia}\n")
        elif "salud" in propuesta:
            salud = consulta_wikipedia("salud preventiva")
            if salud:
                chat_window.insert(tk.END, f"ROBO: {salud}\n")

    if user_input.lower() == 'bye':
        bot_reply = "¡Adiós! Cuídate."
    elif user_input.lower() in ['gracias', 'muchas gracias']:
        bot_reply = "¡De nada!"
    elif greeting(user_input) is not None:
        bot_reply = greeting(user_input)
    else:
        bot_reply = response(user_input)

    chat_window.insert(tk.END, "ROBO: " + bot_reply + "\n")

    turno = {"usuario": user_input, "robo": bot_reply}
    memoria.insert_one(turno)
    historial_conversacion.append(turno)

    repeticiones = sum(1 for t in historial_conversacion if t["usuario"].lower() == user_input.lower())
    if repeticiones >= 3:
        ya_aprendido = aprendizaje.find_one({"pregunta": user_input})
        if not ya_aprendido:
            aprendizaje.insert_one({"pregunta": user_input, "respuesta": bot_reply})

# Exportar historial
def exportar_historial_txt():
    with open("historial_robo.txt", "w", encoding="utf-8") as file:
        for turno in historial_conversacion:
            file.write(f"Tú: {turno['usuario']}\nROBO: {turno['robo']}\n\n")

def exportar_historial_csv():
    with open("historial_robo.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Usuario", "ROBO"])
        for turno in historial_conversacion:
            writer.writerow([turno["usuario"], turno["robo"]])

def exportar_historial_md():
    with open("historial_robo.md", "w", encoding="utf-8") as file:
        file.write("# Historial de conversación con ROBO\n\n")
        for i, turno in enumerate(historial_conversacion, start=1):
            file.write(f"### Conversación {i}\n")
            file.write(f"- **Tú:** {turno['usuario']}\n")
            file.write(f"- **ROBO:** {turno['robo']}\n\n")
    print("Historial exportado a historial_robo.md")

# Editor de aprendizaje supervisado
def abrir_editor_aprendizaje():
    editor = tk.Toplevel(root)
    editor.title("Aprendizaje supervisado")

    preguntas_pendientes = list(aprendizaje.find({"respuesta": None}, {"_id": 0}))

    if not preguntas_pendientes:
        tk.Label(editor, text="No hay preguntas pendientes.").pack(padx=10, pady=10)
        return

    tk.Label(editor, text="Selecciona una pregunta para enseñar a ROBO:").pack(padx=10, pady=5)

    lista = tk.Listbox(editor, width=80)
    for p in preguntas_pendientes:
        lista.insert(tk.END, p["pregunta"])
    lista.pack(padx=10, pady=5)

    respuesta_entry = tk.Entry(editor, width=80)
    respuesta_entry.pack(padx=10, pady=5)
    respuesta_entry.insert(0, "Escribe aquí la respuesta...")

    def guardar_respuesta():
        seleccion = lista.curselection()
        if seleccion:
            pregunta = lista.get(seleccion[0])
            respuesta = respuesta_entry.get()
            if respuesta.strip():
                aprendizaje.update_one({"pregunta": pregunta}, {"$set": {"respuesta": respuesta}})
                tk.Label(editor, text="¡Respuesta guardada! ROBO ha aprendido.").pack(pady=5)

    tk.Button(editor, text="Guardar respuesta", command=guardar_respuesta).pack(pady=5)

# Interfaz gráfica principal
root = tk.Tk()
root.title("Chatbot ROBO")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(padx=10, pady=5)
entry.bind("<Return>", send)

send_button = tk.Button(root, text="Enviar", command=send, font=("Arial", 12))
send_button.pack(pady=5)

btn_explorador = tk.Button(root, text="Modo Explorador", command=activar_explorador, font=("Arial", 12))
btn_explorador.pack(pady=2)

btn_txt = tk.Button(root, text="Exportar a TXT", command=exportar_historial_txt, font=("Arial", 12))
btn_txt.pack(pady=2)

btn_csv = tk.Button(root, text="Exportar a CSV", command=exportar_historial_csv, font=("Arial", 12))
btn_csv.pack(pady=2)

btn_md = tk.Button(root, text="Exportar a Markdown", command=exportar_historial_md, font=("Arial", 12))
btn_md.pack(pady=2)

btn_aprender = tk.Button(root, text="Enseñar a ROBO", command=abrir_editor_aprendizaje, font=("Arial", 12))
btn_aprender.pack(pady=2)

chat_window.insert(tk.END, "ROBO: ¡Hola! Soy ROBO. Pregúntame lo que quieras sobre chatbots. Escribe 'bye' para salir.\n")

root.mainloop()
