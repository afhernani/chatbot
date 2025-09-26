# -*- coding: utf-8 -*-
# pip install nltk scikit-learn pymongo

import tkinter as tk
from tkinter import scrolledtext
import nltk
import random
import string
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

# Cargar corpus en español
with open('chatbot.txt', 'r', errors='ignore', encoding='utf-8') as f:
    raw = f.read().lower()

sent_tokens = nltk.sent_tokenize(raw, language='spanish')
word_tokens = nltk.word_tokenize(raw, language='spanish')

# Preprocesamiento
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens): return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(p), None) for punct in string.punctuation)
def LemNormalize(text): return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict), language='spanish'))

# Saludos
GREETING_INPUTS = ("hola", "buenas", "saludos", "qué tal", "hey")
GREETING_RESPONSES = ["¡Hola!", "¡Hey!", "*asiente*", "Hola, ¿qué tal?", "¡Encantado de hablar contigo!"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generar respuesta
def response(user_response):
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
        robo_response += "Lo siento, no entiendo lo que me dices."
    else:
        robo_response += temp_tokens[idx]
    return robo_response

# Enviar mensaje
def send(event=None):
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_window.insert(tk.END, "Tú: " + user_input + "\n")
    entry.delete(0, tk.END)

    if user_input.lower() == 'bye':
        bot_reply = "¡Adiós! Cuídate."
    elif user_input.lower() in ['gracias', 'muchas gracias']:
        bot_reply = "¡De nada!"
    elif greeting(user_input) is not None:
        bot_reply = greeting(user_input)
    else:
        bot_reply = response(user_input)

    chat_window.insert(tk.END, "ROBO: " + bot_reply + "\n")

    # Guardar en MongoDB
    memoria.insert_one({
        "usuario": user_input,
        "robo": bot_reply
    })

# Interfaz gráfica
root = tk.Tk()
root.title("Chatbot ROBO")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(padx=10, pady=5)
entry.bind("<Return>", send)  # Ejecutar al pulsar Enter

send_button = tk.Button(root, text="Enviar", command=send, font=("Arial", 12))
send_button.pack(pady=5)

chat_window.insert(tk.END, "ROBO: ¡Hola! Soy ROBO. Pregúntame lo que quieras sobre chatbots. Escribe 'bye' para salir.\n")

root.mainloop()
