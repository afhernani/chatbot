# -*- coding: utf-8 -*-
# pip install chatterbot
# pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Crear el chatbot
chatbot = ChatBot('ROBO')

# Entrenador con una lista de frases
trainer = ListTrainer(chatbot)

def cargar_corpus(path):
    with open(path, "r", encoding="utf-8") as f:
        lineas = [line.strip() for line in f if line.strip()]
    corpus = []
    for i in range(0, len(lineas) - 1, 2):
        corpus.append(lineas[i])
        corpus.append(lineas[i + 1])
    return corpus

# Cargar y entrenar por tema
temas = ["faq_salud.txt", "faq_cultura.txt", "faq_tecnologia.txt", "faq_digitalización.txt"]
for archivo in temas:
    corpus = cargar_corpus(archivo)
    trainer.train(corpus)

# Interacción básica
while True:
    entrada = input("Tú: ")
    if entrada.lower() in ["salir", "adiós", "bye"]:
        print("ROBO: ¡Hasta luego!")
        break
    respuesta = chatbot.get_response(entrada)
    # print("ROBO:", respuesta)
    if float(respuesta.confidence) < 0.5:
        print("ROBO: Lo siento, no entiendo tu pregunta.")
    else:
        print("ROBO:", respuesta)