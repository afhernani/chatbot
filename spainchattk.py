# -*- coding: utf-8 -*-
# pip install nltk scikit-learn

import tkinter as tk
from tkinter import scrolledtext
import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Inicialización NLTK
nltk.download('punkt')
nltk.download('wordnet')

# Descargar stopwords en español
nltk.download('stopwords')
from nltk.corpus import stopwords
spanish_stopwords = stopwords.words('spanish')

# Cargar corpus en español
with open('chatbot.txt', 'r', errors='ignore', encoding='utf-8') as f:
    raw = f.read().lower()

# Tokenización en español
sent_tokens = nltk.sent_tokenize(raw, language='spanish')
word_tokens = nltk.word_tokenize(raw, language='spanish')

# Preprocesamiento
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict), language='spanish'))

# Saludos en español
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
    # TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='spanish')
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

# Interfaz gráfica con Tkinter
def send():
    user_input = entry.get()
    chat_window.insert(tk.END, "Tú: " + user_input + "\n")
    entry.delete(0, tk.END)

    if user_input.lower() == 'bye':
        chat_window.insert(tk.END, "ROBO🤖: ¡Adiós! Cuídate.\n")
        return
    elif user_input.lower() in ['gracias', 'muchas gracias']:
        chat_window.insert(tk.END, "ROBO🤖: ¡De nada!\n")
    elif greeting(user_input) is not None:
        chat_window.insert(tk.END, "ROBO🤖: " + greeting(user_input) + "\n")
    else:
        bot_reply = response(user_input)
        chat_window.insert(tk.END, "ROBO🤖: " + bot_reply + "\n")

# Crear ventana principal
root = tk.Tk()
root.title("Chatbot ROBO🤖")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Enviar", command=send, font=("Arial", 12))
send_button.pack(pady=5)

chat_window.insert(tk.END, "ROBO🤖: ¡Hola! Soy ROBO. Pregúntame lo que quieras sobre chatbots. Escribe 'bye' para salir.\n")

root.mainloop()
