# En Base al código de charrterA.py

```py
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
```

# Fortalezas y Debilidades de ChatterA.py

## ¿Qué hace este código?

    Crea un chatbot llamado "ROBO" usando ChatterBot.

    Carga corpus personalizados desde archivos .txt para entrenar al bot.

    Entrena el bot con pares de preguntas y respuestas.

    Inicia una conversación interactiva en consola, respondiendo según el nivel de confianza.

## Estructura esperada de los archivos .txt

Cada archivo debe tener pares de líneas:

```Código
¿Qué es la digitalización?
La digitalización es el proceso de convertir información en formato digital.
```

Este formato permite que el bot aprenda cómo responder a preguntas específicas.

### Fortalezas

    Modularidad: puedes añadir fácilmente nuevos temas.

    Control de confianza: evita respuestas incorrectas si el bot no está seguro.

    Interfaz sencilla: ideal para pruebas rápidas.

## Sugerencias de mejora

Evitar entrenamiento repetido: Si ejecutas el script varias veces, el bot puede sobreentrenarse. Considera guardar el estado del entrenamiento.

Persistencia del chatbot: Usa un storage_adapter como SQLite para conservar el aprendizaje entre sesiones:

```python
chatbot = ChatBot(
    'ROBO',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
```

Manejo de errores: Agrega manejo de excepciones al cargar archivos para evitar fallos si falta alguno.

Interfaz gráfica o web: Puedes integrar el bot en una aplicación Flask o usar una interfaz gráfica con Tkinter para hacerlo más accesible.

Mejorar el corpus: Añade más ejemplos variados y naturales para mejorar la comprensión del bot.

¿Quieres que te ayude a convertir este bot en una aplicación web o añadir funciones como reconocimiento de voz?

------------------------------------------

# HACIENDO ALGO NUEVO.

Vamos a transformar tu bot en algo mucho más interactivo y divertido: un modo juego de preguntas con opciones múltiples, activable por el usuario o sugerido por el bot. Aquí tienes una versión avanzada del código, estructurada profesionalmente, modular y fácil de escalar:

## Objetivo

    Activar un modo juego donde el bot hace preguntas con 3 opciones.

    El usuario puede activar este modo escribiendo algo como "jugar" o el bot puede sugerirlo espontáneamente.

    El bot evalúa la respuesta y da feedback.

## Estructura del código

ejemplo: **reschatbot.py**

```py
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random

# Crear el chatbot con almacenamiento persistente
chatbot = ChatBot(
    'ROBO',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///robo_db.sqlite3'
)

trainer = ListTrainer(chatbot)

# Entrenar con corpus de preguntas frecuentes
def cargar_corpus(path):
    with open(path, "r", encoding="utf-8") as f:
        lineas = [line.strip() for line in f if line.strip()]
    corpus = []
    for i in range(0, len(lineas) - 1, 2):
        corpus.append(lineas[i])
        corpus.append(lineas[i + 1])
    return corpus

temas = ["faq_salud.txt", "faq_cultura.txt", "faq_tecnologia.txt", "faq_digitalización.txt"]
for archivo in temas:
    trainer.train(cargar_corpus(archivo))

# Preguntas para el modo juego
preguntas_juego = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": ["Madrid", "París", "Roma"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué planeta es conocido como el planeta rojo?",
        "opciones": ["Venus", "Marte", "Júpiter"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Quién escribió 'Cien años de soledad'?",
        "opciones": ["Mario Vargas Llosa", "Gabriel García Márquez", "Pablo Neruda"],
        "respuesta_correcta": 1
    }
]

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
        print(f"ROBO: Incorrecto. La respuesta correcta era: {pregunta['opciones'][pregunta['respuesta_correcta']]}")

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
            # Sugerencia de juego si no entiende
            sugerir = random.choice([True, False])
            if sugerir:
                print("ROBO: ¿Quieres jugar conmigo? Escribe 'jugar' para comenzar.")
        else:
            print("ROBO:", respuesta)
```
## ¿Qué puedes hacer a partir de aquí?

    Añadir más preguntas al preguntas_juego desde archivos .json o .csv.

    Crear niveles de dificultad.

    Guardar puntuaciones por sesión.

    Integrar con una interfaz web o móvil.

¿Quieres que te ayude a convertir esto en una app web con Flask o que el bot tenga memoria de puntuaciones por jugador?

_____________________________________

# Sobre el cuerpo entrenado.

Vamos a llevar tu chatbot a un nivel superior: el modo juego ahora se alimentará directamente del corpus temático con el que entrenaste al bot. Eso significa que las preguntas del juego estarán basadas en salud, cultura, tecnología y digitalización.

## ¿Cómo lo haremos?

    Extraer pares de pregunta-respuesta de los archivos .txt que ya usas para entrenar.

    Convertirlos en preguntas tipo test con 3 opciones, una correcta y dos distractores.

    Activar el modo juego cuando el usuario lo solicite o cuando el bot lo sugiera.

## Código mejorado

ejemplo: **reschatbot2.py**
```py
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
```

## ¿Qué puedes añadir?

    Niveles de dificultad según el tema.

    Puntuación acumulada por sesión.

    Modo competitivo entre usuarios.

    Exportar preguntas a JSON para usarlas en apps web o móviles.

¿Quieres que te ayude a convertir esto en una app web con Flask o que el bot tenga memoria de puntuaciones por jugador?

_________________________________________


