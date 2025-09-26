# -*- coding: utf-8 -*-
# pip install chatterbot
# pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Crear el chatbot
chatbot = ChatBot('ROBO')

# Entrenador con una lista de frases
trainer = ListTrainer(chatbot)

# Frases de entrenamiento
conversacion = [
    "Hola",
    "Hola, ¿cómo estás?",
    "¿Cuál es tu nombre?",
    "Me llamo ROBO, encantado de conocerte.",
    "¿Qué puedes hacer?",
    "Puedo conversar contigo y aprender de tus preguntas.",
    "Adiós",
    "¡Hasta luego!"
]

faq_salud = [
    "¿Qué es la hipertensión?",
    "La hipertensión es una condición en la que la presión arterial está elevada de forma crónica.",
    "¿Cómo prevenir la diabetes?",
    "Mantener una dieta equilibrada, hacer ejercicio regularmente y evitar el sobrepeso son claves para prevenirla."
]

faq_cultura = [
    "¿Qué es el flamenco?",
    "El flamenco es un arte musical y de danza originario de Andalucía.",
    "¿Quién fue Miguel de Cervantes?",
    "Fue un escritor español, autor de 'Don Quijote de la Mancha'."
]

faq_tecnologia = [
    "¿Qué es la inteligencia artificial?",
    "Es la capacidad de una máquina para imitar funciones cognitivas humanas como el aprendizaje.",
    "¿Qué es un chatbot?",
    "Un chatbot es un programa que simula una conversación con humanos mediante texto o voz."
]

# Entrenar con cada tema
trainer.train(faq_salud)
trainer.train(faq_cultura)
trainer.train(faq_tecnologia)
trainer.train(conversacion)

# Función para cargar FAQs desde un archivo .txt
def cargar_faq_desde_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    return [line.strip() for line in lineas if line.strip()]

# Interacción básica
while True:
    entrada = input("Tú: ")
    if entrada.lower() in ["salir", "adiós", "bye"]:
        print("ROBO: ¡Hasta luego!")
        break
    respuesta = chatbot.get_response(entrada)
    print("ROBO:", respuesta)
