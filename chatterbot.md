# Chatterbot

Crear un chatbot con Python es totalmente posible y muy flexible. Puedes hacerlo desde algo básico hasta sistemas avanzados con inteligencia artificial. Aquí te muestro cómo empezar paso a paso:

## Chatbot básico con ChatterBot

ChatterBot es una librería ideal para principiantes. Permite entrenar un bot con ejemplos de conversación sin necesidad de programar reglas complejas.

### Ejemplo simple:
```python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Crear el chatbot
bot = ChatBot('Asistente')

# Entrenamiento con frases básicas

trainer = ListTrainer(bot)
conversacion = [
    'Hola',
    'Hola, ¿cómo puedo ayudarte?',
    '¿Cuál es tu nombre?',
    'Me llamo Asistente, encantado de conocerte.'
]
trainer.train(conversacion)

# Probar el chatbot
print(bot.get_response('Hola'))
```

## Puedes ampliar el entrenamiento con más frases o conectarlo a una interfaz web.

## Chatbot avanzado con Rasa

Rasa es una plataforma profesional en Python para crear chatbots con procesamiento de lenguaje natural (NLP), gestión de contexto y despliegue en producción.

Permite crear flujos de conversación complejos.

Se integra con canales como WhatsApp, Telegram o web.

Requiere conocimientos más avanzados, pero es muy potente.

## Procesamiento de texto con SpaCy o NLTK

Si quieres que tu bot entienda mejor el lenguaje humano, puedes usar librerías como:

SpaCy: para reconocimiento de entidades, análisis sintáctico, etc.

NLTK: para tokenización, clasificación de texto y respuestas automáticas.

## Recursos útiles para aprender

Guía paso a paso para crear un chatbot en Python – KeepCoding

Tutorial de ChatterBot en español – DataCamp

Ejemplo con NLTK – CódigoFuente.org

¿Quieres que te ayude a diseñar un flujo de conversación específico para tu chatbot en Python o elegir la mejor librería según tu nivel? Estoy listo para ayudarte a construirlo paso a paso.

_____________________________________________________

# Chatbot

Un chatbot (también conocido como bot, chatterbot, IM bot, agente interactivo o Entidad de conversación artificial) es un programa de computadora o inteligencia artificial que realiza una conversación a través de métodos auditivos o textuales. Dichos programas a menudo están diseñados para simular de manera convincente cómo se comportaría un ser humano como un compañero de conversación, por lo que pasa la prueba de Turing.

Los chatbots se utilizan normalmente en sistemas de diálogo para diversos propósitos prácticos, incluido el servicio al cliente o la adquisición de información.


Algunos chatbots utilizan sistemas sofisticados de procesamiento de lenguaje natural, pero muchos sistemas más simples buscan palabras clave dentro de la entrada, luego extraen una respuesta con las palabras clave más coincidentes, o el patrón de redacción más similar, de una base de datos.

Si quieres crear chatbots más avanzados con procesamiento del lenguaje natural puedes probar la plataforma ChatCompose. La plataforma te ofrece herramientas para crear un chatbot web, y chatbot desktop entre otros.

En este post aprenderemos a crear un simple asistente de chat o chatbot utilizando la biblioteca NLTK de Python.

NLTK tiene un módulo, **nltk.chat**, que simplifica la creación de estos motores al proporcionar un marco genérico.

En este blog estoy usando 2 importaciones de nltk.chat.util:

**Chat:** esta es una clase que tiene toda la lógica que usa el chatbot.

**Reflections:** Este es un diccionario que contiene un conjunto de valores de entrada y sus valores de salida correspondientes. Es un diccionario opcional que puedes usar. También puedes crear tu propio diccionario en el mismo formato que se muestra a continuación y utilizarlo en tu código.

También puedes crear tu propio diccionario de reflexiones en el siguiente formato y utilizarlo en su código. Aquí hay un ejemplo:

```py
mis_reflexions = {
"ir": "fui",
"hola": "hey"
}

```

Y usarlo así:

```py
chat = Chat(pares, mis_reflexions)
```

Usando el concepto anterior de la biblioteca NLTK de python, construyamos un chatbot simple sin usar ninguno de los Algoritmos de Aprendizaje Automático o Aprendizaje Profundo. Así que obviamente nuestro chatbot será decente pero no inteligente.

Código fuente:

```py
from nltk.chat.util import Chat, reflections
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?",]
    ],
     [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot ?",]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?",]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
],
]
def chatear():
    print("Hola soy un bot, escribe algo para comenzar") #mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    chat.converse()
if __name__ == "__main__":
    chatear()
```

El código es bastante simple, aún así te lo explicamos.

Una vez que se invoca la función chatear(), se mostrará un mensaje predeterminado:

```bash
>Hola soy un bot, escribe algo para comenzar
>
```
Los chatbots nltk.chat trabajan con la expresión regular de las palabras clave presentes en tu pregunta. Por lo tanto, puedes agregar cualquier número de preguntas en un formato adecuado para que tu chatbot no se confunda al determinar la expresión regular.

______________________________________________________________________________

# Procesamiento Básico de Datos con Python

Los requisitos de programación en la ciencia de datos exigen un lenguaje muy versátil pero flexible que sea simple para escribir el código pero que pueda manejar un procesamiento matemático altamente complejo. Python es más adecuado para estos requisitos, ya que ya se ha establecido como un lenguaje para la informática general y científica. 

Además, se está actualizando continuamente en forma de una nueva adición a su gran cantidad de bibliotecas destinadas a diferentes requisitos de programación.

Los siguientes, son fragmentos de Python que pueden ser útiles para principiantes para algunas tareas de procesamiento de datos diferentes.

Las [tareas del procesamiento de datos](https://www.tecnologias-informacion.com/procesamientodatos.html) van desde procesamiento de texto y listas básico a procesamiento de conjunto de datos con Pandas.

## Concatenar varios archivos de texto

Comencemos con la concatenación de varios archivos de texto. Si tienes varios archivos de texto en un solo directorio que necesitas concatenar en un solo archivo, este código Python lo hará.

Primero obtenemos una lista de todos los archivos txt en la ruta; luego leemos en cada archivo y escribimos su contenido en el nuevo archivo de salida; finalmente, volvemos a leer el nuevo archivo e imprimimos su contenido en la pantalla para verificarlo.

```py
import glob 
# Cargar todos los archivos txt en la ruta 
files = glob.glob ('/ path / to / files / *. txt') 
# Concatenar archivos a un nuevo archivo 
with open('2020_output.txt', 'w') as out_file:
    for file_name in files:
        with open(file_name) as in_file:
            out_file.write(in_file.read())
# Leer archivo e imprimir 
with open('2020_output.txt', 'r') as new_file:
    lines = [line.strip() for line in new_file]
for line in lines:
    print(line)
```

la salida:

```bash
archivo 1 línea 1 
archivo 1 línea 2 
archivo 1 línea 3 
archivo 2 línea 1 
archivo 2 línea 2 
archivo 2 línea 3 
archivo 3 línea 1 
archivo 3 línea 2 
archivo 3 línea 3
```

## Concatenar varios archivos CSV en un marco de datos

Siguiendo con el tema de la concatenación de archivos, esta vez abordemos la concatenación de varios archivos de valores separados por comas en un solo marco de datos de Pandas.

Primero obtenemos una lista de los archivos CSV en nuestra ruta; luego, para cada archivo en la ruta, leemos el contenido en su propio marco de datos; luego, combinamos todos los marcos de datos en un solo marco; finalmente, imprimimos los resultados para inspeccionar.

```py
import glob 
# Cargar todos los archivos csv en la ruta 
files = glob.glob ('/ path/to/files/ *. csv') 
# Crear una lista de dataframe, una serie por CSV 
fruit_list = [] 
for file_name in files: 
    df = pd.read_csv (file_name, index_col = None, header = None) 
    fruit_list.append (df) 
# Crear un marco combinado a partir de la lista de marcos individuales 
fruit_frame = pd.concat (fruit_list, axis = 0, ignore_index = True) 
print (fruit_frame)
```

## Aplanar listas

Quizás tengas una situación en la que estés trabajando con una lista de listas, es decir, una lista en la que todos sus elementos también sean listas. Este fragmento tomará esta lista de listas incrustadas y la acoplará a una lista lineal.

Primero crearemos una lista de listas para usar en nuestro ejemplo; luego usaremos listas por comprensión para aplanar la lista de una manera Pythonic; finalmente, imprimimos la lista resultante en la pantalla para su verificación.

```py
# Creación de lista de listas (una lista donde todos sus elementos son listas)
list_of_lists = [['manzana', 'pera', 'plátano', 'uvas'], ['cebra', 'burro', 'elefante', 'vaca'],['vainilla', 'chocolate'], ['princesa', 'Príncipe']]
# Aplanar la lista de listas en una sola lista
flat_list = [element for sub_list in list_of_lists for element in sub_list]
# Imprime ambos para comparar
print(f'List of lists:\n{list_of_lists}')
print(f'Flattened list:\n{flat_list}')
```

## Imprimiendo pantalla verás

```bash
Lista de listas: 

[[‘manzana’, ‘pera’, ‘plátano’, ‘uvas’], [‘cebra’, ‘burro’, ‘elefante’, ‘vaca’], [‘vainilla’, ‘chocolate’] , [‘princesa’, ‘príncipe’]] 

Lista plana: 

[‘manzana’, ‘pera’, ‘plátano’, ‘uvas’, ‘cebra’, ‘burro’, ‘elefante’, ‘vaca’, ‘vainilla’ , ‘chocolate’, ‘princesa’, ‘príncipe’]
```

## Ordenar lista de tuplas

Este fragmento considerará la idea de ordenar tuplas según el elemento especificado. Las tuplas son una estructura de datos de Python que a menudo se pasa por alto y son una excelente manera de almacenar datos relacionados sin usar un tipo de estructura más complejo.

En este ejemplo, primero crearemos una lista de tuplas de tamaño 2 y las llenaremos con datos numéricos; a continuación clasificaremos los pares, por separado por el primer y segundo elemento, imprimiendo los resultados de ambos procesos de clasificación para inspeccionar los resultados; finalmente, ampliaremos esta clasificación a elementos de datos alfanuméricos mixtos.

```py
# Algunos datos emparejados
pares = [(1, 10.5), (5, 7.), (2, 12.7), (3, 9.2), (7, 11.6)]
# Ordenar pares por primera entrada
sorted_pairs = sorted (pares, clave = lambda x: x [0])
print (f'Ordenado por elemento 0 (primer elemento): \ n {sorted_pairs} ')
# Ordenar pares por segunda entrada
sorted_pairs = sorted (pares, clave = lambda x: x [1])
print (f'Ordenado por elemento 1 (segundo elemento): \ n {sorted_pairs} ')
# Extiende esto a tuplas de tamaño n y entradas no numéricas
pares = [('banana', 3), ('manzana', 11), ('pera', 1), ('sandía', 4), ('fresa', 2), ('kiwi', 12) ]
sorted_pairs = sorted (pares, clave = lambda x: x [0])
print (f'Apares alfanuméricos ordenados por elemento 0 (primer elemento): \ n {sorted_pairs} ')
```

## Imprimiendo pantalla verás

Ordenado por elemento 0 (primer elemento):
```py
[(1, 10,5), (2, 12,7), (3, 9,2), (5, 7,0), (7, 11,6)]

Ordenado por elemento 1 (segundo elemento):

[(5, 7.0), (3, 9.2), (1, 10.5), (7, 11.6), (2, 12.7)]

Pares alfanuméricos ordenados por elemento 0 (primer elemento):

[(‘manzana’, 11), (‘plátano’, 3), (‘kiwi’, 12), (‘pera’, 1), (‘fresa’, 2), (‘sandía’, 4)]

```

# Procesamiento de datos con Pandas

Trabajaremos con un [conjunto de datos](https://www.kaggle.com/rhuebner/human-resources-data-set/home) de 310 empleados activos y despedidos junto con información como estado civil, género, departamento, tasa de pago, estado, puesto, etc. 

## Análisis Básico

```py
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import make_pipeline
from feature_engine import missing_data_imputers as mdi
from feature_engine import categorical_encoders as ce
from sklearn.model_selection import train_test_split
%matplotlib inline
with open('HRDataset.csv') as f:
    df = pd.read_csv(f)
f.close()
df.head()
df.info()
```

Al cargar nuestros datos, podemos ver una serie de tipos de características únicas. Tenemos características categóricas como “Employee_Name” y “Position”. Tenemos funciones binarias como “MarriedID”. Tenemos características continuas como “PayRate” y “EmpSatisfaction”.

Tenemos funciones discretas como “DaysLateLast30” y finalmente tenemos funciones de fecha como “LastPerformanceReview_Date”.

## Variabilidad de características alta o baja

El primer paso que suelo dar es revisar el recuento único de valores por característica para determinar si alguna característica se puede eliminar rápidamente debido a una variabilidad muy alta o muy baja.

En otras palabras, ¿tenemos características que tengan tantos valores únicos como la longitud del conjunto de datos o características que tengan un solo valor único?

```py
for col in df.columns:
  print(col, df[col].nunique(), len(df))
```

Podemos eliminar con seguridad “Employee_Name”, “Emp_ID”, “DOB” ya que la mayoría, si no todos, los valores son únicos para cada función. Además, podemos eliminar “DaysLateLast30” ya que esta característica solo contiene un valor único.

```py
df.drop(['Employee_Name'], axis=1, inplace=True)
df.drop(['EmpID'], axis=1, inplace=True)
df.drop(['DOB'], axis=1, inplace=True)
df.drop(['DaysLateLast30'], axis=1, inplace=True)
```
## Funciones duplicadas

A continuación, al examinar el libro de códigos, que contiene las definiciones de cada función, podemos ver que tenemos muchas funciones duplicadas.

Por ejemplo, “MarriedStatusID” es una función numérica que produce el código que coincide con los estatutos de casados en la función “MaritalDesc”. Podemos eliminar estas características.

```py
df.drop(['MaritalStatusID', 'EmpStatusID', 'DeptID'], axis=1, inplace=True)
df.drop(['GenderID'], axis=1, inplace=True)
df.drop(['PerformanceScore'], axis=1, inplace=True)
df.drop(['MarriedID'], axis=1, inplace=True)
```

____________________________________________

# ChatterBot

## Paso 1: Instalar ChatterBot

Primero, instala las librerías necesarias:

```bash
pip install chatterbot
pip install chatterbot_corpus
```

## Paso 2: Código básico del chatbot

ejemplo: **chatter.py**

```python
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

trainer.train(conversacion)

# Interacción básica
while True:
    entrada = input("Tú: ")
    if entrada.lower() in ["salir", "adiós", "bye"]:
        print("ROBO: ¡Hasta luego!")
        break
    respuesta = chatbot.get_response(entrada)
    print("ROBO:", respuesta)
```

## ¿Qué puedes hacer después?

    Entrenar con más frases o importar corpus en español.

    Integrar con una interfaz gráfica (Tkinter) o web (Flask).

    Guardar el estado del chatbot para que aprenda con el tiempo.

¿Quieres que lo conectemos con una interfaz visual como hiciste con Tkinter? O que lo entrenemos con corpus más avanzados como FAQs o temas específicos (salud, cultura, tecnología). Tú eliges el siguiente paso.

________________________________________________

¡Excelente decisión, Hernani! Entrenar tu chatbot con corpus temáticos como FAQs de salud, cultura y tecnología lo hará mucho más útil y especializado. Aquí te explico cómo hacerlo paso a paso:

## ¿Dónde conseguir corpus temáticos?
Aquí tienes fuentes confiables con contenido en español:

| Tema |	Fuente recomendada |
|---------------|---------------|
| Salud |	[MedlinePlus en español](https://medlineplus.gov/spanish/) – Sección de preguntas frecuentes |
| Cultura  |  [Instituto Cervantes](https://cvc.cervantes.es/) – Artículos y glosarios culturales |
| Tecnología  |  [Xataka](https://www.xataka.com/) o [FAQ de productos tecnológicos](https://support.google.com/) |

También puedes explorar corpus académicos como:

[CORPES XXI de la RAE](https://www.rae.es/banco-de-datos/corpes-xxi) – Corpus general con textos reales en español.

[Corpus del Español](https://www.corpusdelespanol.org/) – Incluye géneros y dialectos variados.

## Cómo estructurar tus datos para ChatterBot
ChatterBot funciona mejor con pares de pregunta-respuesta. Puedes crear listas como esta:

```python

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
```
## Entrenamiento con ChatterBot

```python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('ROBO')
trainer = ListTrainer(chatbot)

# Entrenar con cada tema
trainer.train(faq_salud)
trainer.train(faq_cultura)
trainer.train(faq_tecnologia)
```

## ¿Y si tienes muchos datos?

Puedes guardar tus pares en archivos .txt o .json y cargarlos dinámicamente:

```python
def cargar_faq_desde_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    return [line.strip() for line in lineas if line.strip()]
```
## ¿Siguiente paso?

¿Quieres que te ayude a crear un corpus temático desde cero? Puedo generar un conjunto de preguntas y respuestas en salud, cultura y tecnología para que lo entrenes directamente. También podemos integrar esto en tu interfaz Tkinter si lo deseas. ¿Cómo quieres continuar?

_______________________________________________

# Implementación corpus temático ChatterBot.

Vamos a implementar una carga dinámica de corpus temáticos para entrenar tu chatbot con ChatterBot. Esto te permitirá mantener tus datos en archivos .txt separados por tema (salud, cultura, tecnología) y cargarlos automáticamente desde tu script.

## Paso 1: Estructura de los archivos .txt

Cada archivo debe tener pares de pregunta-respuesta, alternando líneas:

Ejemplo: `faq_salud.txt`
```bash
Código
¿Qué es la hipertensión?
La hipertensión es una condición médica en la que la presión arterial se mantiene elevada de forma crónica.
¿Cómo prevenir la diabetes tipo 2?
Mantener una dieta equilibrada, hacer ejercicio regularmente y controlar el peso ayuda a prevenirla.
...
```

Haz lo mismo para `faq_cultura.txt` y `faq_tecnologia.txt`.

## Paso 2: Función para cargar dinámicamente

```python
def cargar_corpus(path):
    with open(path, "r", encoding="utf-8") as f:
        lineas = [line.strip() for line in f if line.strip()]
    corpus = []
    for i in range(0, len(lineas) - 1, 2):
        corpus.append(lineas[i])
        corpus.append(lineas[i + 1])
    return corpus
```

## Paso 3: Entrenar el chatbot con los archivos

```python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('ROBO')
trainer = ListTrainer(chatbot)

# Cargar y entrenar por tema
temas = ["faq_salud.txt", "faq_cultura.txt", "faq_tecnologia.txt"]
for archivo in temas:
    corpus = cargar_corpus(archivo)
    trainer.train(corpus)
```
ejemplo: **chatterA.py**

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
temas = ["faq_salud.txt", "faq_cultura.txt", "faq_tecnologia.txt"]
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
    print("ROBO:", respuesta)
    if float(respuesta.confidence) < 0.5:
        print("ROBO: Lo siento, no entiendo tu pregunta.")

```

¿Quieres que te genere los archivos .txt con contenido listo para copiar y pegar?
Puedo prepararte los tres archivos con 10 pares de preguntas y respuestas por tema. También puedo ayudarte a integrarlo en tu interfaz Tkinter para que ROBO use este corpus temático. ¿Te gustaría que avancemos con eso?


_______________________________________________

# Solución paso a paso

Activa tu entorno nlp:

    conda activate nlp


Descarga el modelo de spaCy en inglés:

    python -m spacy download en_core_web_sm


Verifica la instalación:

    python -m spacy validate


Deberías ver algo como:

    Loaded model 'en_core_web_sm'

## Alternativa (instalar como paquete pip)

También puedes instalar el modelo directamente como paquete:

pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl

## Nota importante

ChatterBot no se actualiza mucho y a veces tiene problemas con versiones nuevas de spaCy.
Si te sigue dando errores, puede que necesites instalar una versión compatible:

pip install spacy==3.5.3


y luego:

python -m spacy download en_core_web_sm


¿Quieres que te arme un requirements.txt o environment.yml con versiones compatibles entre chatterbot y spacy para que no te vuelva a dar conflictos?

_______________________________________________

# Cómo extraer preguntas y respuestas de una página web.

Para extraer automáticamente preguntas y respuestas de sitios web y convertirlas en corpus .txt para ChatterBot, vamos a seguir este enfoque:

# Estrategia de extracción automática

## Identificar fuentes confiables

Ya tenemos estas fuentes:

Salud:[ASISA](https://www.asisa.es/preguntas-frecuentes/biblioteca-de-salud)

Cultura: [Clara.es](https://www.clara.es/estilo-de-vida/600-preguntas-sobre-cultura-general-mas-comunes-y-sus-respuestas-para-compartir_25783)

Tecnología: [Sujeto.es](https://sujeto.es/50-preguntas-sobre-tecnologia-con-respuestas/)

## Usar Python para hacer scraping

Utilizaremos `requests` y `BeautifulSoup` para extraer contenido HTML y convertirlo en pares de pregunta-respuesta.

## Guardar como corpus .txt

Cada archivo tendrá líneas alternas: pregunta, respuesta, pregunta, respuesta…

## Ejemplo de extractor para tecnología (Sujeto.es)

ejemplo: **sujeto.py**

```python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def extraer_tecnologia():
    url = "https://sujeto.es/50-preguntas-sobre-tecnologia-con-respuestas/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    preguntas_respuestas = []
    for p in soup.find_all("p"):
        texto = p.get_text().strip()
        if texto.startswith("¿") or texto.startswith("¿Qué"):
            preguntas_respuestas.append(texto)
        elif texto and len(preguntas_respuestas) % 2 == 1:
            preguntas_respuestas.append(texto)

    with open("faq_tecnologia.txt", "w", encoding="utf-8") as f:
        for linea in preguntas_respuestas:
            f.write(linea + "\n")

extraer_tecnologia()
```

## Resultado

El archivo faq_tecnologia.txt tendrá este formato:

Código

```txt
¿Qué es un algoritmo?
Un algoritmo es un conjunto de instrucciones paso a paso para resolver un problema.
¿Qué es la inteligencia artificial?
Es la capacidad de una máquina para imitar funciones humanas como el aprendizaje.
...
```

## ¿Qué sigue?
¿Quieres que prepare extractores similares para salud y cultura?

¿Prefieres que los corpus se guarden en una carpeta específica?

¿Te gustaría que el script entrene automáticamente a ROBO después de generar los archivos?

Puedo ayudarte a montar todo el flujo completo. Tú decides cómo avanzamos.

_________________________________________________________________

# Flujo de dialogo

Perfecto, Hernani. Vamos a diseñar un flujo de conversación para un chatbot de atención al cliente en un negocio local, por ejemplo, una tienda de ropa. Este flujo puede adaptarse fácilmente a otros sectores.

## Ejemplo de flujo de conversación: Tienda de ropa

### Inicio
Bot: ¡Hola! 👋 Bienvenido a [Nombre de la tienda]. ¿En qué puedo ayudarte hoy? Opciones:

Ver productos

Consultar disponibilidad 

Horarios y ubicación 

Hablar con un asesor 

### Ver productos

Bot: ¿Qué tipo de productos te interesan? Opciones:

Ropa de mujer

Ropa de hombre

Accesorios

Ofertas

Bot: Aquí tienes algunas opciones populares. ¿Quieres ver más o filtrar por talla o color?


### Consultar disponibilidad

Bot: ¿Qué producto quieres consultar? Puedes escribir el nombre o enviar una foto. Usuario: “Vestido rojo talla M” Bot: 
¡Perfecto! El vestido rojo talla M está disponible. ¿Quieres reservarlo o comprarlo?

### Horarios y ubicación

Bot: Estamos abiertos de lunes a sábado de 10:00 a 20:00. 📍 Nuestra tienda está en Calle Mayor 123, Las Palmas. ¿Quieres ver cómo llegar?

### Hablar con un asesor
Bot: Un asesor estará contigo en breve. Mientras tanto, ¿quieres dejar tu nombre y número de contacto?

### Cierre
Bot: ¿Hay algo más en lo que pueda ayudarte? Opciones:

Sí, volver al menú principal

No, gracias.

¿Quieres que te ayude a crear este flujo en una herramienta como Landbot o ManyChat? También puedo adaptarlo a tu tipo de negocio si me cuentas un poco más.

_______________________________________________________________

¿Qué herramientas puedo usar para crear este flujo?
¡Buena pregunta, Hernani! Aquí tienes algunas herramientas populares y efectivas para crear flujos de conversación sin necesidad de saber programar:

Herramientas sin código (fáciles de usar)

| Herramienta	| Ideal para...	  | Características destacadas  |
|---------------|-------------------|----------------------------|
| Landbot |	Web, WhatsApp, formularios interactivos |	Editor visual tipo drag & drop, muy intuitivo |
| ManyChat	| Facebook Messenger, Instagram, WhatsApp  |	Automatización con etiquetas, CRM integrado |
| Tidio   |	Web y e-commerce (Shopify, WooCommerce)  |	Chat en vivo + chatbot, integración con tiendas |
| Chatfuel  |	Facebook Messenger  |	Flujos simples, integración con APIs externas |
| BotStar  |	Multicanal (web, Messenger, etc.)   |	Plantillas listas para usar, analíticas integradas  |


## Herramientas con código (más flexibles)

| Herramienta | 	Lenguaje/Framework  | 	Ideal para...   |
|--------------------|-------------------------|-----------------------|

| Dialogflow (Google) |	Node.js, Python	 | Bots inteligentes con NLP avanzado |
| Rasa	| Python |  Chatbots personalizados y privados |
| Botpress  |	JavaScript  |	Interfaz visual + control total  |
| Microsoft Bot Framework |	C#, Node.js  |	Integración con Azure y Teams |

### ¿Cuál elegir?

Si quieres algo rápido y visual, empieza con Landbot o ManyChat.

Si buscas control total y privacidad, ve por Rasa o Botpress.

Si tu negocio está en Instagram o Facebook, ManyChat es ideal.

Si vendes online, Tidio se integra muy bien con tiendas.

¿Quieres que te ayude a construir tu primer flujo en alguna de estas herramientas? Puedo guiarte paso a paso.

___________________________________________________________________________________

# Rasa and python

Rasa es una de las plataformas más potentes para crear chatbots personalizados con Python. Aquí te explico cómo empezar paso a paso:

## ¿Qué es Rasa?
Rasa es un framework open source para construir chatbots y asistentes virtuales con procesamiento de lenguaje natural (NLP). Te permite tener control total sobre el flujo, la lógica y los datos.

### Componentes clave de Rasa


| Componente  |	Función principal |
|---------------|-----------------|
| Rasa NLU	|  Entiende lo que dice el usuario (intenciones, entidades) |
| Rasa Core	|    Decide cómo responder (gestiona el diálogo) |
| [Domain.yml]   |	Define respuestas, acciones, intents y entidades |
| Stories.yml   |	Ejemplos de conversaciones para entrenar el bot  |
| Actions.py  |	Código Python para acciones personalizadas  |


## Cómo crear tu chatbot con Rasa

###  Instala Rasa

```bash
pip install rasa
```

### Crea tu proyecto

```bash
rasa init
```
Esto genera una estructura básica con ejemplos.

### Define tu dominio

Edita domain.yml para incluir:

	Intents (ej. saludo, consulta)

	Entities (ej. producto, fecha)

	Responses (mensajes del bot)

	Actions (acciones personalizadas)

## Entrena el modelo

```bash
rasa train
```

## Prueba el bot en local

```bash
rasa shell
```

## Ejecuta acciones personalizadas
```bash
rasa run actions
```

## Integraciones posibles

	WhatsApp, Telegram, Messenger

	Webchat (con Botfront o Rasa Webchat)

	APIs externas (CRM, bases de datos, etc.)

## Consejos útiles

Usa Rasa X para mejorar el bot con conversaciones reales.

Añade validaciones para formularios.

Implementa acciones personalizadas para lógica avanzada.

¿Quieres que te ayude a crear un flujo básico en Rasa o escribir un ejemplo de domain.yml y stories.yml para tu negocio?

______________________________________________________________________

# rasa in python 3.9

1. Crear entorno virtual con Anaconda
Abre Anaconda Prompt y ejecuta:

```bash
conda create -n rex python=3.9
conda activate rex
```

Rasa funciona mejor con Python 3.9. Evita 3.10+ por compatibilidad.

## Instalar dependencias clave

Primero actualiza pip y setuptools:

```bash
pip install --upgrade pip setuptools wheel
```
Luego instala Rasa:

```bash
pip install rasa
```

## Verifica instalación

Comprueba que Rasa está instalado:

```bash
rasa --version
```

Deberías ver algo como:

```Código
Rasa 3.x.x
Python 3.8.x
```

## Crear tu proyecto Rasa

```bash
rasa init --no-prompt
```

Esto crea una carpeta con:

    data/nlu.yml → para tus corpus temáticos

    data/rules.yml → reglas de conversación

    domain.yml → intents, respuestas, entidades

    actions.py → lógica personalizada

## Añadir corpus temático

Edita data/nlu.yml y añade tus preguntas por tema:

```yaml
version: "3.1"
nlu:
- intent: salud
  examples: |
    - ¿Qué es la hipertensión?
    - ¿Cómo prevenir la diabetes tipo 2?
    - ¿Qué síntomas tiene la gripe?

- intent: cultura
  examples: |
    - ¿Quién fue Miguel de Cervantes?
    - ¿Qué es el flamenco?
    - ¿Qué representa el Día de los Muertos?

- intent: tecnologia
  examples: |
    - ¿Qué es la inteligencia artificial?
    - ¿Qué es un chatbot?
    - ¿Qué es el Big Data?
```
##  Entrenar y probar

```bash
rasa train
rasa shell
```

Tu bot ya puede responder por temas. Si quieres que reconozca entidades o dé respuestas específicas, podemos editar domain.yml y responses.

¿Quieres que te prepare un paquete con corpus .yml por tema para que lo pegues directamente en tu proyecto Rasa? También puedo ayudarte a conectar Rasa con tu interfaz Tkinter o convertirlo en app web. Tú eliges el siguiente paso.


_____________
# Definiendo domain.yml y stores.yml

¡Vamos allá, Hernani! Te ayudaré a crear los archivos esenciales para tu chatbot en Rasa: domain.yml y stories.yml. Supongamos que tu negocio es una tienda de ropa y el bot atiende consultas sobre productos, horarios y contacto.

domain.yml — Define el comportamiento del bot

```yaml
version: "3.1"

intents:
  - saludo
  - consulta_productos
  - consulta_horarios
  - contacto_humano
  - despedida

entities:
  - producto

slots:
  producto:
    type: text
    influence_conversation: true

responses:
  utter_saludo:
    - text: "¡Hola! Bienvenido a nuestra tienda 👗 ¿En qué puedo ayudarte hoy?"

  utter_consulta_productos:
    - text: "¿Qué tipo de producto estás buscando? Puedes decirme el nombre o categoría."

  utter_consulta_horarios:
    - text: "Abrimos de lunes a sábado de 10:00 a 20:00. ¿Quieres saber cómo llegar?"

  utter_contacto_humano:
    - text: "Un asesor estará contigo en breve. ¿Quieres dejar tu nombre y número?"

  utter_despedida:
    - text: "¡Gracias por visitarnos! Si necesitas algo más, aquí estaré 😊"

actions:
  - action_buscar_producto
```

stories.yml — Ejemplos de conversaciones

```stories.yml
version: "3.1"
stories:
  - story: flujo de saludo y consulta
    steps:
      - intent: saludo
      - action: utter_saludo
      - intent: consulta_productos
      - action: utter_consulta_productos
      - action: action_buscar_producto

  - story: consulta de horarios
    steps:
      - intent: consulta_horarios
      - action: utter_consulta_horarios

  - story: contacto humano
    steps:
      - intent: contacto_humano
      - action: utter_contacto_humano

  - story: despedida
    steps:
      - intent: despedida
      - action: utter_despedida
```
¿Quieres que te ayude a crear el archivo nlu.yml con ejemplos de frases que el bot debe entender? También puedo ayudarte a escribir la acción personalizada action_buscar_producto en Python. Tú eliges el siguiente paso.

Aquí tienes los archivos que completan tu chatbot en Rasa para una tienda de ropa:

nlu.yml — Entrenamiento de lenguaje natural

Este archivo enseña al bot a reconocer las intenciones del usuario y extraer entidades como el nombre del producto.

```yaml
version: "3.1"
nlu:
  - intent: saludo
    examples: |
      - hola
      - buenos días
      - qué tal
      - hey
      - buenas tardes

  - intent: consulta_productos
    examples: |
      - quiero ver vestidos
      - tienes camisetas negras
      - estoy buscando pantalones
      - ¿hay chaquetas de cuero?
      - quiero comprar un [vestido rojo](producto)
      - ¿tienes [camisa blanca](producto)?

  - intent: consulta_horarios
    examples: |
      - cuál es el horario
      - a qué hora abren
      - están abiertos hoy
      - horario de la tienda

  - intent: contacto_humano
    examples: |
      - quiero hablar con alguien
      - necesito ayuda de un asesor
      - me puede atender una persona
      - contacto humano

  - intent: despedida
    examples: |
      - gracias
      - adiós
      - hasta luego
      - nos vemos
```

actions.py — Acción personalizada para buscar productos
Este archivo ejecuta lógica personalizada cuando el usuario pregunta por un producto.
```python
# -*- coding: utf-8 -*-
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBuscarProducto(Action):

    def name(self) -> Text:
        return "action_buscar_producto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        producto = tracker.get_slot("producto")

        if producto:
            # Simulación de búsqueda en inventario
            disponibles = ["vestido rojo", "camisa blanca", "pantalón negro"]
            if producto.lower() in disponibles:
                dispatcher.utter_message(text=f"¡Sí! Tenemos {producto} disponible. ¿Quieres reservarlo?")
            else:
                dispatcher.utter_message(text=f"Lo siento, no tenemos {producto} en este momento.")
        else:
            dispatcher.utter_message(text="¿Podrías decirme qué producto estás buscando?")

        return []
```
Vamos a completar tu bot con los últimos dos archivos esenciales:

## rules.yml — Reglas para respuestas directas

Este archivo permite que el bot responda automáticamente a ciertas intenciones sin depender de historias largas.

```yaml
version: "3.1"
rules:
  - rule: Saludo inicial
    steps:
      - intent: saludo
      - action: utter_saludo

  - rule: Consulta de horarios
    steps:
      - intent: consulta_horarios
      - action: utter_consulta_horarios

  - rule: Solicitud de contacto humano
    steps:
      - intent: contacto_humano
      - action: utter_contacto_humano

  - rule: Despedida
    steps:
      - intent: despedida
      - action: utter_despedida

```

## Cómo probar tu bot en local

### Entrena el modelo

```bash
rasa train
```

###. Ejecuta el bot en modo conversación

```bash
rasa shell
```

### Ejecuta el servidor de acciones personalizadas

```bash
rasa run actions
```

### (Opcional) Usa Rasa X para mejorar el bot

```bash
rasa x
```
## ¿Cómo conectarlo a una interfaz web o WhatsApp?

## 🔹 Webchat

	Usa Rasa Webchat

	Integra el script en tu sitio web:

```html
<script src="https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.js"></script>
<script>
  WebChat.default({
    initPayload: "/saludo",
    customData: { language: "es" },
    socketUrl: "http://localhost:5005",
    title: "Asistente de tienda",
    subtitle: "¿En qué puedo ayudarte?"
  });
</script>
```

## 🔹 WhatsApp

	Usa Twilio + WhatsApp Business API

	Conecta Twilio con tu bot mediante webhook en `credentials.yml`

¿Quieres que te ayude a configurar el archivo `credentials.yml` para conectar con Twilio o desplegar el bot en un servidor? También puedo ayudarte a crear una interfaz visual para tus clientes. Tú decides el siguiente paso.


______________________________________________________________________________________________________


# Configurar `credentials.yml`


Vamos a completar lo que necesitas: conectar tu bot de Rasa con Twilio para WhatsApp y desplegarlo en un servidor. Aquí tienes una guía clara para ambas tareas:

## Conectar Rasa con Twilio y WhatsApp

### Crea una cuenta en Twilio
Ve a [twilio.com](https://www.twilio.com/)

Activa el Sandbox de WhatsApp desde el panel de Twilio

Sigue las instrucciones para unirte al sandbox (normalmente enviando un código por WhatsApp)

## Configura `credentials.yml` en Rasa

Agrega esta sección al archivo credentials.yml:

```yaml
twilio:
  account_sid: "TU_ACCOUNT_SID"
  auth_token: "TU_AUTH_TOKEN"
  phone_number: "whatsapp:+14155238886"
```

### Reemplaza los valores con los que te da Twilio en tu panel.

### Ejecuta el bot con Twilio

```bash
rasa run --connector twilio --enable-api
```

Tu bot ya puede recibir y responder mensajes por WhatsApp desde el sandbox.

# Desplegar Rasa en un servidor (Linux o VPS)

Opción rápida: Usar Docker

##Instala Docker y Docker Compose

```bash
sudo apt update
sudo apt install docker docker-compose
```

## Crea un archivo docker-compose.yml

```yaml
version: '3.0'
services:
  rasa:
    image: rasa/rasa:latest
    ports:
      - "5005:5005"
    volumes:
      - ./rasa:/app
    command: run --enable-api

  action_server:
    image: rasa/rasa-sdk:latest
    ports:
      - "5055:5055"
    volumes:
      - ./rasa/actions:/app/actions
```
### Estructura de carpetas

```Código
/rasa
  /actions
    actions.py
  domain.yml
  data/
  models/
  config.yml
  credentials.yml
  endpoints.yml
```

## Levanta los servicios

```bash
docker-compose up -d
```

## Recomendaciones para producción

Usa ngrok o Nginx para exponer el puerto 5005 públicamente.

Protege tu bot con HTTPS usando Let's Encrypt.

Usa Rasa Enterprise si necesitas escalabilidad, roles de usuario o analíticas avanzadas.

¿Quieres que te ayude a configurar el archivo `endpoints.yml` o a crear un webhook para recibir mensajes desde WhatsApp? También puedo ayudarte a probarlo en tu móvil. ¡Vamos paso a paso!