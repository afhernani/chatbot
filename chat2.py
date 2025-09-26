# -*- coding: utf-8 -*-
# pip install nltk scikit-learn

import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Descargar recursos necesarios de NLTK
nltk.download('punkt')     # Tokenizador de oraciones
nltk.download('wordnet')   # Lemmatizador

# Descargar stopwords en español
nltk.download('stopwords')
from nltk.corpus import stopwords
spanish_stopwords = stopwords.words('spanish')

# Leer el corpus base
with open('chatbot.txt', 'r', errors='ignore', encoding='utf-8') as f:
    raw = f.read().lower()

# Tokenización en español
sent_tokens = nltk.sent_tokenize(raw, language='spanish')
word_tokens = nltk.word_tokenize(raw, language='spanish')

# Tokenización
# sent_tokens = nltk.sent_tokenize(raw)  # Lista de oraciones
# word_tokens = nltk.word_tokenize(raw)  # Lista de palabras

# Lematización y normalización
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Respuestas a saludos
#GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
#GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

# Saludos en español
GREETING_INPUTS = ("hola", "buenas", "saludos", "qué tal", "hey")
GREETING_RESPONSES = ["¡Hola!", "¡Hey!", "*asiente*", "Hola, ¿qué tal?", "¡Encantado de hablar contigo!"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generación de respuesta basada en similitud coseno
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    # TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=spanish_stopwords)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        robo_response += "lo siento! No te entiendo."
    else:
        robo_response += sent_tokens[idx]

    sent_tokens.remove(user_response)
    return robo_response

# Bucle principal del chatbot
def start_chat():
    print("ROBO: mi nombre es ROBO. ¡Pregúntame lo que quieras! (Escribe 'bye' para salir)")
    while True:
        user_response = input().lower()
        if user_response == 'bye':
            print("ROBO: Adios! ten cuidado.")
            break
        elif user_response in ['gracias', 'te lo agradezco']:
            print("ROBO: se bien venido!")
            break
        elif greeting(user_response) is not None:
            print("ROBO:", greeting(user_response))
        else:
            print("ROBO:", response(user_response))

# Ejecutar chatbot
if __name__ == "__main__":
    start_chat()
