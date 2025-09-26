# -*- coding: utf-8 -*-
# pip install nltk spacy pymongo requests scikit-learn
# python -m spacy download es_core_news_md

import tkinter as tk
from tkinter import scrolledtext
import nltk
import random
import string
import csv
import requests
from pymongo import MongoClient
import spacy
from spacy.lang.es.stop_words import STOP_WORDS
spanish_stopwords = STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Descarga de recursos de NLTK
def descargar_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    # Elimina la descarga de wordnet y stopwords
    # try:
    #     nltk.data.find('corpora/wordnet')
    # except LookupError:
    #     nltk.download('wordnet')
    # try:
    #     nltk.data.find('corpora/stopwords')
    # except LookupError:
    #     nltk.download('stopwords')

descargar_nltk()

# Inicialización spaCy
nlp = spacy.load("es_core_news_md")

# Procesamiento de texto
remove_punct_dict = dict((ord(p), None) for p in string.punctuation)
def LemTokens(tokens):
    return [token.lemma_ for token in nlp(" ".join(tokens))]

def LemNormalize(text):
    tokens = [t.text for t in nlp(text.lower().translate(remove_punct_dict))]
    return LemTokens(tokens)

# Saludos
GREETING_INPUTS = ("hola", "buenas", "saludos", "qué tal", "hey")
GREETING_RESPONSES = ["¡Hola!", "¡Hey!", "Hola, ¿qué tal?", "¡Encantado de hablar contigo!"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Respuestas variables
RESPUESTAS_GRACIAS = ["¡De nada!", "Siempre a tu servicio.", "No hay de qué.", "¡Un placer ayudarte!"]
RESPUESTAS_DESPEDIDA = ["¡Hasta pronto!", "Cuídate mucho.", "Nos vemos luego.", "¡Adiós! Fue un gusto."]


def respuesta_variable(tipo):
    if tipo == "gracias":
        return random.choice(RESPUESTAS_GRACIAS)
    elif tipo == "bye":
        return random.choice(RESPUESTAS_DESPEDIDA)

# Reconocimiento emocional
def detectar_emocion(texto):
    emociones = {
        "triste": ["triste", "deprimido", "mal", "llorando"],
        "feliz": ["feliz", "contento", "alegre", "genial"],
        "enojado": ["enojado", "molesto", "furioso", "rabia"]
    }
    for emocion, palabras in emociones.items():
        if any(p in texto.lower() for p in palabras):
            return emocion
    return None

def respuesta_emocional(emocion):
    frases = {
        "triste": "Siento que estés así. ¿Quieres que hablemos de algo que te anime?",
        "feliz": "¡Me alegra mucho saberlo! ¿Compartes qué te tiene tan contento?",
        "enojado": "Vaya, parece que algo te molestó. ¿Quieres desahogarte conmigo?"
    }
    return frases.get(emocion)

# Seguimiento conversacional
def seguimiento():
    frases = [
        "¿Quieres saber más sobre eso?",
        "¿Te gustaría que te cuente algo relacionado?",
        "Si quieres, puedo explicarlo con más detalle.",
        "¿Te interesa otro tema parecido?"
    ]
    return random.choice(frases)

class EstadoConversacion:
    def __init__(self):
        self.modo_explorador = False
        self.contexto_reciente = []

    def actualizar_contexto(self, turno):
        self.contexto_reciente.append(turno)
        if len(self.contexto_reciente) > 3:
            self.contexto_reciente.pop(0)

    def referencia_implicita(self, user_input):
        if not isinstance(user_input, str):
            return "Entrada no válida."
        if user_input.lower() in ["¿y eso?", "¿por qué?", "¿cómo así?"]:
            if self.contexto_reciente and "robo" in self.contexto_reciente[-1]:
                return f"Creo que te refieres a esto: “{self.contexto_reciente[-1]['robo']}”"
        return None

estado = EstadoConversacion()

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["chatmemory"]
    memoria = db["conversaciones"]
    aprendizaje = db["aprendizaje"]
except Exception as e:
    print(f"Error de conexión a MongoDB: {e}")
    memoria = None
    aprendizaje = None

# Cargar historial de conversación
if memoria is not None:
    historial_conversacion = list(memoria.find({}, {"_id": 0}))
else:
    historial_conversacion = []

# Verificar existencia y contenido de chatbot.txt
corpus_path = "chatbot.txt"
mensaje_corpus = ""
if not os.path.exists(corpus_path):
    mensaje_corpus = "El archivo chatbot.txt no existe. Por favor, crea el archivo con frases para el chatbot."
    raw = ""
elif os.path.getsize(corpus_path) == 0:
    mensaje_corpus = "El archivo chatbot.txt está vacío. Por favor, agrega frases para el chatbot."
    raw = ""
else:
    with open(corpus_path, "r", encoding="utf-8") as file:
        raw = file.read().lower()

if raw:
    sent_tokens = nltk.sent_tokenize(raw)
else:
    sent_tokens = []

# Opcional: añadir frases del historial
for turno in historial_conversacion:
    sent_tokens.append(turno["robo"])

def respuesta_spacy(user_input):
    if not sent_tokens:
        return None, 0
    doc_input = nlp(user_input)
    similitudes = [(texto, doc_input.similarity(nlp(texto))) for texto in sent_tokens]
    similitudes.sort(key=lambda x: x[1], reverse=True)
    mejor_texto, mejor_sim = similitudes[0]

    # Si la pregunta es tipo "¿qué es ...?" busca la palabra clave en el corpus
    if user_input.lower().startswith("¿que es") or user_input.lower().startswith("que es"):
        palabras_usuario = [w.lower() for w in user_input.split() if w.isalpha()]
        for frase in sent_tokens:
            for palabra in palabras_usuario:
                if palabra in frase.lower():
                    return frase, 0.99  # Similitud artificial alta para forzar respuesta
        # Si no encuentra, sigue con la similitud normal

    # Si la similitud es baja, intenta búsqueda por palabra clave
    if mejor_sim < 0.52:
        palabras_usuario = [w.lower() for w in user_input.split() if w.isalpha()]
        for frase in sent_tokens:
            for palabra in palabras_usuario:
                if palabra in frase.lower():
                    return frase, 0.51
        return mejor_texto, mejor_sim
    return mejor_texto, mejor_sim

def generar_respuesta(user_input):
    # Emoción
    emocion = detectar_emocion(user_input)
    if emocion:
        return respuesta_emocional(emocion)
    # Referencia implícita
    referencia = estado.referencia_implicita(user_input)
    if referencia:
        return referencia
    # Despedida
    if user_input.lower() == 'bye':
        return respuesta_variable("bye")
    # Agradecimiento
    if user_input.lower() in ['gracias', 'muchas gracias']:
        return respuesta_variable("gracias")
    # Saludo
    saludo = greeting(user_input)
    if saludo is not None:
        return saludo
    # 1. Aprendizaje supervisado
    resultado = aprendizaje.find_one({"pregunta": {"$regex": user_input, "$options": "i"}})
    if resultado and resultado["respuesta"]:
        return resultado["respuesta"]
    # 2. Corpus (spaCy similitud + palabra clave)
    texto_similar, sim = respuesta_spacy(user_input)
    if texto_similar and sim >= 0.52:
        return texto_similar
    elif texto_similar:
        if aprendizaje is not None:
            aprendizaje.insert_one({"pregunta": user_input, "respuesta": None})
        return f"No estoy seguro, pero quizás te refieres a:\n→ {texto_similar}\nLo guardaré para aprender más adelante."
    # 3. Historial de conversación
    for turno in reversed(historial_conversacion):
        if user_input.lower() in turno["usuario"].lower():
            return turno["robo"]
    # 4. Wikipedia
    respuesta_api = consulta_wikipedia(user_input)
    if respuesta_api:
        return respuesta_api
    # 5. Clima
    if "clima" in user_input or "tiempo" in user_input:
        ciudad = obtener_ciudad(user_input)
        clima = consulta_clima(ciudad)
        if clima:
            return clima
    # 6. Curiosidad
    if "fecha" in user_input or "día" in user_input:
        curiosidad = consulta_curiosidad("9/20")
        if curiosidad:
            return curiosidad
    # 7. Mensaje por defecto
    return "No sé cómo responder a eso todavía, pero lo guardaré para aprender."

def send(event=None):
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_window.insert(tk.END, "Tú: " + user_input + "\n")
    entry.delete(0, tk.END)

    # Modo explorador
    if estado.modo_explorador:
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

    bot_reply = generar_respuesta(user_input)

    chat_window.insert(tk.END, "ROBO: " + bot_reply + "\n")
    chat_window.insert(tk.END, "ROBO: " + seguimiento() + "\n")

    # Si es despedida, cerrar ventana
    if user_input.lower() == 'bye':
        root.after(1000, root.destroy)
        return

    turno = {"usuario": user_input, "robo": bot_reply}

    # Evitar duplicados en conversaciones
    if memoria is not None:
        existe = memoria.find_one({"usuario": {"$regex": f"^{user_input}$", "$options": "i"}})
        if not existe:
            memoria.insert_one(turno)

    # Evitar duplicados en aprendizaje
    if aprendizaje is not None:
        repeticiones = sum(1 for t in historial_conversacion if t["usuario"].lower() == user_input.lower())
        ya_aprendido = aprendizaje.find_one({"pregunta": user_input})
        if repeticiones >= 3 and not ya_aprendido:
            aprendizaje.insert_one({"pregunta": user_input, "respuesta": bot_reply})

    historial_conversacion.append(turno)
    estado.actualizar_contexto(turno)

# APIs externas
def consulta_wikipedia(pregunta):
    url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{pregunta.replace(' ', '_')}"
    try:
        r = requests.get(url)
        data = r.json()
        if 'extract' in data:
            return data['extract']
    except Exception as e:
        print(f"Error Wikipedia: {e}")
        return None

def consulta_clima(ciudad):
    clave = "f05e56d95b36745a1b52e03462f5c701"
    if clave == "f05e56d95b36745a1b52e03462f5c701":
        return "No se ha configurado la clave de OpenWeather."
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave}&units=metric&lang=es"
    try:
        r = requests.get(url)
        data = r.json()
        if data.get("main"):
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"En {ciudad} hay {desc} con {temp}°C."
        elif data.get("message"):
            return f"No se pudo obtener el clima: {data['message']}"
    except Exception as e:
        print(f"Error Clima: {e}")
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
    clave = "f1e054cf970c4d61a290dafbc2a3d723"
    url = f"https://newsapi.org/v2/top-headlines?country=es&category=general&apiKey={clave}"
    try:
        r = requests.get(url)
        data = r.json()
        if data.get("articles"):
            return data["articles"][0]["title"]
        elif data.get("message"):
            return f"No se pudo obtener noticias: {data['message']}"
    except Exception as e:
        print(f"Error Noticias: {e}")
        return None

def obtener_ciudad(user_response):
    doc = nlp(user_response)
    for ent in doc.ents:
        if ent.label_ == "LOC" or ent.label_ == "GPE":
            return ent.text
    palabras = user_response.split()
    for palabra in reversed(palabras):
        if palabra.lower() not in spanish_stopwords and palabra.isalpha():
            return palabra
    return "Madrid"  # Valor por defecto

# Modo explorador
def activar_explorador():
    estado.modo_explorador = not estado.modo_explorador
    estado_texto = "activado" if estado.modo_explorador else "desactivado"
    chat_window.insert(tk.END, f"ROBO: Modo explorador {estado_texto}.\n")

def sugerir_tema():
    temas = [
        "¿Sabías que el cerebro humano consume el 20% de la energía del cuerpo?",
        "¿Quieres saber qué pasó un día como hoy en la historia?",
        "¿Te interesa conocer una curiosidad científica?",
        "¿Te cuento una noticia cultural actual?",
        "¿Te gustaría saber algo sobre salud preventiva?"
    ]
    return random.choice(temas)

# Función principal de respuesta


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

# Editor de aprendizaje supervisado
def abrir_editor_aprendizaje():
    editor = tk.Toplevel(root)
    editor.title("Aprendizaje supervisado")

    preguntas_pendientes = list(aprendizaje.find({}, {"_id": 0}))

    tk.Label(editor, text="Selecciona una pregunta para enseñar a ROBO:").pack(padx=10, pady=5)

    lista = tk.Listbox(editor, width=80)
    for p in preguntas_pendientes:
        lista.insert(tk.END, p["pregunta"])
    lista.pack(padx=10, pady=5)

    respuesta_entry = tk.Entry(editor, width=80)
    respuesta_entry.pack(padx=10, pady=5)
    respuesta_entry.insert(0, "Escribe aquí la respuesta...")

    estado_label = tk.Label(editor, text="")
    estado_label.pack(pady=5)

    def actualizar_respuesta(event):
        seleccion = lista.curselection()
        estado_label.config(text="")  # Borra el mensaje al seleccionar otra pregunta
        if seleccion:
            pregunta = lista.get(seleccion[0])
            registro = aprendizaje.find_one({"pregunta": pregunta})
            if registro and registro.get("respuesta"):
                respuesta_entry.delete(0, tk.END)
                respuesta_entry.insert(0, registro["respuesta"])
            else:
                respuesta_entry.delete(0, tk.END)
                respuesta_entry.insert(0, "null")

    lista.bind("<<ListboxSelect>>", actualizar_respuesta)

    def guardar_respuesta():
        seleccion = lista.curselection()
        if seleccion:
            pregunta = lista.get(seleccion[0])
            respuesta = respuesta_entry.get()
            if respuesta.strip():
                aprendizaje.update_one({"pregunta": pregunta}, {"$set": {"respuesta": respuesta}})
                estado_label.config(text="¡Respuesta guardada! ROBO ha aprendido.")
            else:
                estado_label.config(text="La respuesta no puede estar vacía.")

    tk.Button(editor, text="Guardar respuesta", command=guardar_respuesta).pack(pady=5)

    # Campo para añadir nueva pregunta manualmente
    nueva_pregunta_entry = tk.Entry(editor, width=80)
    nueva_pregunta_entry.pack(padx=10, pady=5)
    nueva_pregunta_entry.insert(0, "Añade una nueva pregunta...")

    def agregar_pregunta():
        pregunta = nueva_pregunta_entry.get()
        if pregunta.strip():
            existe = aprendizaje.find_one({"pregunta": pregunta})
            if not existe:
                aprendizaje.insert_one({"pregunta": pregunta, "respuesta": None})
                lista.insert(tk.END, pregunta)
                lista.selection_clear(0, tk.END)
                lista.selection_set(tk.END)
                lista.activate(tk.END)
                respuesta_entry.delete(0, tk.END)
                respuesta_entry.insert(0, "null")
                estado_label.config(text="Pregunta añadida. Ahora puedes enseñarle la respuesta.")
            else:
                estado_label.config(text="Esa pregunta ya existe en el aprendizaje.")

    tk.Button(editor, text="Añadir pregunta", command=agregar_pregunta).pack(pady=5)

# Interfaz gráfica principal
root = tk.Tk()
root.title("Chatbot ROBO")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

if mensaje_corpus:
    chat_window.insert(tk.END, f"ROBO: {mensaje_corpus}\n")

entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(padx=10, pady=5)
entry.bind("<Return>", send)

# Primer grupo de botones (Enviar, Enseñar a ROBO, Modo Explorador)
frame_superior = tk.Frame(root)
frame_superior.pack(pady=5)

send_button = tk.Button(frame_superior, text="Enviar", command=send, font=("Arial", 12))
send_button.pack(side=tk.LEFT, padx=5)

btn_aprender = tk.Button(frame_superior, text="Enseñar a ROBO", command=abrir_editor_aprendizaje, font=("Arial", 12))
btn_aprender.pack(side=tk.LEFT, padx=5)

btn_explorador = tk.Button(frame_superior, text="Modo Explorador", command=activar_explorador, font=("Arial", 12))
btn_explorador.pack(side=tk.LEFT, padx=5)

# Segundo grupo de botones (Exportar a TXT, CSV, Markdown)
frame_exportar = tk.Frame(root)
frame_exportar.pack(pady=5)

btn_txt = tk.Button(frame_exportar, text="Exportar a TXT", command=exportar_historial_txt, font=("Arial", 12))
btn_txt.pack(side=tk.LEFT, padx=5)

btn_csv = tk.Button(frame_exportar, text="Exportar a CSV", command=exportar_historial_csv, font=("Arial", 12))
btn_csv.pack(side=tk.LEFT, padx=5)

btn_md = tk.Button(frame_exportar, text="Exportar a Markdown", command=exportar_historial_md, font=("Arial", 12))
btn_md.pack(side=tk.LEFT, padx=5)

# Botón salir debajo
btn_salir = tk.Button(root, text="Salir", command=root.destroy, font=("Arial", 12))
btn_salir.pack(pady=10)

chat_window.insert(tk.END, "ROBO: ¡Hola! Soy ROBO. Pregúntame lo que quieras sobre chatbots. Escribe 'bye' para salir.\n")

root.mainloop()