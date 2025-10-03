# -*- coding: utf-8 -*-
# pip install chatterbot
# pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
import os

# Crear el chatbot con almacenamiento persistente
chatbot = ChatBot(
    'ROBO',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///robo_db.sqlite3'
)

trainer = ListTrainer(chatbot)

# Cargar corpus y entrenar
def cargar_corpus(path):
    with open(path, "r", encoding="utf-8") as f:
        lineas = [line.strip() for line in f if line.strip()]
    corpus = []
    for i in range(0, len(lineas) - 1, 2):
        corpus.append(lineas[i])
        corpus.append(lineas[i + 1])
    return corpus

# Generar preguntas tipo test desde corpus
def generar_preguntas_test(corpus):
    preguntas = []
    for i in range(0, len(corpus) - 1, 2):
        pregunta = corpus[i]
        respuesta_correcta = corpus[i + 1]
        distractores = random.sample([r for j, r in enumerate(corpus[1::2]) if r != respuesta_correcta], 2)
        opciones = distractores + [respuesta_correcta]
        random.shuffle(opciones)
        preguntas.append({
            "pregunta": pregunta,
            "opciones": opciones,
            "respuesta_correcta": opciones.index(respuesta_correcta)
        })
    return preguntas

# Cargar y entrenar corpus temáticos
temas = ["faq_salud.txt", "faq_cultura.txt", "faq_tecnologia.txt", "faq_digitalización.txt"]
preguntas_juego = []

for archivo in temas:
    if os.path.exists(archivo):
        corpus = cargar_corpus(archivo)
        trainer.train(corpus)
        preguntas_juego.extend(generar_preguntas_test(corpus))

# Modo juego
def jugar():
    pregunta = random.choice(preguntas_juego)
    print("\nROBO: ¡Vamos a jugar! Responde la siguiente pregunta:")
    print("ROBO:", pregunta["pregunta"])
    for i, opcion in enumerate(pregunta["opciones"], 1):
        print(f"{i}. {opcion}")
    eleccion = input("Tu respuesta (1/2/3): ")
    if not eleccion.isdigit() or int(eleccion) not in [1, 2, 3]:
        print("ROBO: Esa no es una opción válida.")
    elif int(eleccion) - 1 == pregunta["respuesta_correcta"]:
        print("ROBO: ¡Correcto! 🎉")
    else:
        correcta = pregunta["opciones"][pregunta["respuesta_correcta"]]
        print(f"ROBO: Incorrecto. La respuesta correcta era: {correcta}")

# Interacción principal
modo_juego = False

while True:
    entrada = input("\nTú: ")
    if entrada.lower() in ["salir", "adiós", "bye"]:
        print("ROBO: ¡Hasta luego!")
        break
    elif entrada.lower() in ["jugar", "modo juego", "quiero jugar"]:
        modo_juego = True
        jugar()
        modo_juego = False
    else:
        respuesta = chatbot.get_response(entrada)
        if float(respuesta.confidence) < 0.5:
            print("ROBO: Lo siento, no entiendo tu pregunta.")
            if random.choice([True, False]):
                print("ROBO: ¿Quieres jugar conmigo? Escribe 'jugar' para comenzar.")
        else:
            print("ROBO:", respuesta)
