# El error dice que falta el recurso 
averaged_perceptron_tagger_eng, no solo el viejo 

## averaged_perceptron_tagger.
Esto es porque en las versiones más nuevas de NLTK (>=3.8), los POS taggers se renombraron para ser específicos por idioma.

### Solución rápida

En tu script, antes de usar pos_tag, descarga explícitamente el nuevo recurso:

```python
# -*- coding: utf-8 -*-

import nltk

nltk.download('punkt')  # para tokenizar
nltk.download('averaged_perceptron_tagger_eng')  # el nuevo tagger de inglés

texto = "NLTK is a powerful library for natural language processing"
tokens = nltk.word_tokenize(texto)
tags = nltk.pos_tag(tokens)

print(tags)
```

## Ajustar tu función de verificación automática

Si quieres mantener el enfoque de "descargar si falta", puedes adaptarla así:

```python
# -*- coding: utf-8 -*-

import nltk
from nltk.data import find
from nltk import word_tokenize, pos_tag

def ensure_nltk_resource(resource):
    try:
        find(resource)
    except LookupError:
        print(f"Recurso {resource} no encontrado. Descargando...")
        nltk.download(resource.split("/")[-1])

# Asegurar tokenizer y tagger
ensure_nltk_resource("tokenizers/punkt")
ensure_nltk_resource("taggers/averaged_perceptron_tagger_eng")

# Ejemplo de uso

texto = "NLTK is a powerful library for natural language processing"
tokens = word_tokenize(texto)
tags = pos_tag(tokens)

print("Tokens:", tokens)
print("Etiquetas POS:", tags)
```

En resumen:

Antes se usaba averaged_perceptron_tagger.

Ahora en NLTK nuevo necesitas averaged_perceptron_tagger_eng para inglés.

________________________________________


# spaCy vs NLTK - Tokenización, etiquetado POS y detección de entidades

El funcionamiento de las dos bibliotecas de Python y las ventajas que esto genera para su empresa son, por tanto, evidentes. ¿Cómo es la aplicación práctica para los desarrolladores? Echemos un vistazo a la tokenización, el etiquetado de partes de la oración y la detección de entidades, tres técnicas esenciales de la PLN que se utilizan en varias fases del procesamiento del lenguaje:

# Tokenización

La tokenización es el primer paso del procesamiento PLN. Los desarrolladores la utilizan para dividir un texto en unidades más pequeñas, denominadas tokens. Estos tokens pueden ser palabras, signos de puntuación u otras unidades lingüísticas. Esto facilita el tratamiento de los textos. Sólo después de la tokenización pueden los programadores someter el texto a otros pasos de procesamiento.

## Tokenización con spaCy

El siguiente ejemplo muestra cómo llevar a cabo la tokenización con spaCy:

```python
# -*- coding: utf-8 -*-

import spacy
# Load the spaCy model for the English language
nlp = spacy.load("en_core_web_sm")
# Sample text to be tokenized
text = "SpaCy is a powerful Python library for natural language processing."
# Process the text using spaCy
doc = nlp(text)
# Tokenize the text and print each token
for token in doc:
    print(token.text)
```

En este ejemplo, utilizamos el modelo en_core_web_sm para tokenizar el texto de muestra. El objeto NLP procesa el texto y, a continuación, cada token del documento procesado se expulsa en un bucle. Puede sustituir la variable "text" por cualquier texto que desee tokenizar con spaCy.

## Tokenización con NLTK

En NLTK, un ejemplo de tokenización tiene este aspecto:

```python
# -*- coding: utf-8 -*-

import nltk
# Sample text for tokenization
text = "NLTK is a leading platform for building Python programs to work with human language data."
# Tokenize the text into words
tokens = nltk.word_tokenize(text)
# Print the tokens
print(tokens)
```

En este código, primero importamos la biblioteca nltk y luego definimos una cadena de texto de ejemplo que queremos tokenizar: "NLTK es una plataforma líder para crear programas Python para procesar datos del lenguaje humano".

La función `nltk.word_tokenize()` se utiliza para convertir el texto de entrada en palabras individuales. Cuando se ejecuta el código, la variable tokens contiene una lista de tokens que representan cada palabra del texto de entrada. Esta es la salida que obtendría si visualizara la lista de tokens:

```bash
['NLTK', 'is', 'a', 'leading', 'platform', 'for', 'building', 'Python', 'programs', 'to', 'work', 'with', 'human', 'language', 'data', '.']
```
En esta salida, NLTK ha tokenizado el texto de entrada en palabras individuales. Cada palabra de esta lista es un elemento. Los signos de puntuación, como los puntos, también se consideran fichas independientes en este proceso.

## Etiquetado de partes de la oración (POS)

La tokenización suele ir seguida del etiquetado de las partes de la oración. Se asignan partes gramaticales a los tokens, como sustantivos, verbos y adjetivos. Esta información es importante para comprender la estructura sintáctica de una frase. El etiquetado de las partes de la oración es especialmente útil para tareas como Análisis de textostraducción de textos y generación de lenguaje, ya que ayuda a comprender la relación entre las palabras de la frase.

# Etiquetado de partes de la oración (POS) con spaCy

Un ejemplo de código para llevar a cabo el etiquetado POS con spaCy tiene este aspecto:

```python
# -*- coding: utf-8 -*-

import spacy
# Load the spaCy model (English)
nlp = spacy.load("en_core_web_sm")
# Sample text for POS tagging
text = "SpaCy is a popular Python library for natural language processing."
# Process the text using spaCy
doc = nlp(text)
# Print the token and its POS tag for each word in the text
for token in doc:
    print(token.text, token.pos_)
```    
En este ejemplo, utilizamos el modelo en_core_web_sm para el procesamiento del inglés. El objeto NLP procesa el texto de entrada y, a continuación, emite las etiquetas POS para cada token del texto con token.text y token.pos_. 

## Etiquetado de partes de la oración (POS) con NLTK

Con NLTK, el etiquetado POS tiene este aspecto, por ejemplo:

```python
# -*- coding: utf-8 -*-

import nltk
from nltk import word_tokenize, pos_tag
# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Sample text
text = "NLTK is a powerful library for natural language processing."
# Perform POS tagging
pos_tags = pos_tag(word_tokenize(text))
# Display the POS tags
print(pos_tags)
```

En este ejemplo, utilizamos la función pos_tag para asignar etiquetas POS a los tokens. Las etiquetas POS consisten en tuplas, donde cada tupla contiene una palabra y la etiqueta POS correspondiente.

# Detección de entidades

La detección de entidades es otra etapa del procesamiento de la PLN cuyo objetivo es reconocer y clasificar entidades con nombre, como personas, lugares, organizaciones y otra información específica en el texto. La detección de entidades permite extraer información importante del texto y es especialmente útil para aplicaciones como la indexación automática de documentos y los sistemas de respuesta a preguntas.

## Detección de entidades con spaCy

La detección de entidades se realiza con spaCy de esta forma, por ejemplo:

```python
# -*- coding: utf-8 -*-

import spacy
# Load the spaCy model for English
nlp = spacy.load("en_core_web_sm")
# Sample text for entity detection
text = "Apple Inc. was founded by Steve Jobs in Cupertino. The iPhone was released in 2007."
# Process the text with spaCy
doc = nlp(text)
# Iterate through the entities and print them
for ent in doc.ents:
    print(f"Entity: {ent.text}, Type: {ent.label_}")
```
En este ejemplo, cargamos el modelo SpaCy en lengua inglesa (en_core_web_sm), procesamos el texto de muestra y, a continuación, recorremos las entidades reconocidas, imprimiendo tanto el texto de la entidad como el tipo de entidad correspondiente. Los tipos de entidad pueden incluir categorías como nombres de personas, organizaciones y lugares.

## Detección de entidades con NLTK

Con NLTK, la detección de entidades para el mismo ejemplo tiene este aspecto:
```python
# -*- coding: utf-8 -*-

import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
# Sample text
text = "Barack Obama was born in Hawaii. He served as the 44th President of the United States."
# Perform part-of-speech tagging
pos_tags = pos_tag(word_tokenize(text))
# Perform named entity recognition
tree = ne_chunk(pos_tags)
# Display named entities
for subtree in tree:
    if isinstance(subtree, nltk.Tree):
        entity = " ".join([word for word, tag in subtree.leaves()])
        label = subtree.label()
        print(f"Entity: {entity}, Label: {label}")
```
En este ejemplo, utilizamos la función ne_chunk para identificar entidades con nombre en el texto. El resultado es una estructura de árbol. Recorremos el árbol para extraer y expulsar las entidades con nombre junto con sus etiquetas.

# spaCy y NLTK - Uso eficiente con **Konfuzio**

Konfuzio dispone de un SDK en Python que permite a los desarrolladores programar sus propios flujos de trabajo documentales. De este modo, podrá aplicar la funcionalidad de spaCy y NLTK a los documentos, exactamente como lo necesite para su caso de uso individual. 

Konfuzio no sólo permite analizar grandes volúmenes de texto en documentos, sino también reconocer y procesar elementos de diseño. Para ello, el proveedor alemán se basa en tecnologías pioneras como PNL, OCR, Aprendizaje automático y Visión por ordenador.

En la práctica, Konfuzio es, por tanto, adecuado para todos los sectores en los que las empresas necesitan procesar grandes volúmenes de datos procedentes de documentos. 

Un ejemplo clásico es su uso en el sector jurídico. Los bufetes de abogados utilizan flujos de trabajo documentales individualizados para analizar, estructurar y clasificar documentos jurídicos. De este modo, los abogados pueden comprender eficazmente los textos jurídicos, extraer los términos clave e identificar la información relevante. Esto reduce el tiempo de procesamiento por caso y, por tanto, ahorra costes.

¿Aún tiene preguntas sobre el uso de Konfuzio para el procesamiento del lenguaje natural? Póngase en contacto con uno de nuestros expertos.

___________________________________________________

# Tecnicas claves para el procesamiento de texto nlp

## Introducción

¿Sabías que el 90% de los datos en el mundo están en formato no estructurado, como texto?

Las técnicas de procesamiento de texto en NLP nos permiten extraer valor de estos datos, transformando el texto en información útil.

¡Sigue leyendo para conocerlas y comenzar a aplicarlas!

## Qué es el procesamiento de texto en NLP

El Procesamiento de Lenguaje Natural (NLP) es una disciplina clave dentro de la inteligencia artificial que se centra en la interacción entre las computadoras y el lenguaje humano. Este proceso permite que las máquinas interpreten el lenguaje humano de manera que puedan interactuar eficazmente con las personas y realizar tareas específicas basadas en texto.

El procesamiento de texto es fundamental en la inteligencia artificial y el análisis de datos por varias razones:

**Automatización de tareas:** Permite automatizar tareas que antes requerían intervención humana, como la clasificación de correos electrónicos, la traducción de idiomas y la moderación de contenido en redes sociales.

**Mejora de la interacción humano-máquina:** Los sistemas como chatbots y asistentes virtuales dependen del procesamiento de texto para entender y responder a las consultas de los usuarios de manera natural y coherente.

**Análisis de datos:** Ayuda a extraer información valiosa de grandes volúmenes de datos textuales, como opiniones de clientes, tendencias en redes sociales y análisis de sentimientos.
 

## Tokenización

La tokenización es una técnica fundamental en el Procesamiento de Lenguaje Natural (NLP) que implica dividir un texto en unidades más pequeñas llamadas tokens.

Estos tokens pueden ser palabras, frases o incluso caracteres individuales, dependiendo del nivel de granularidad requerido. La tokenización es el primer paso en muchas tareas de NLP, ya que facilita el análisis y procesamiento posterior del texto.

## Qué es la tokenización

La tokenización consiste en segmentar un texto en componentes básicos que pueden ser procesados por algoritmos de NLP. Los tokens son las unidades mínimas que conservan significado en el contexto del texto.

Por ejemplo, en la frase **“El procesamiento de lenguaje natural es todo un mundo”**, los tokens serían **[“El”, “procesamiento”, “de”, “lenguaje”, “natural”, “es”, “todo”, “un”, “mundo”]**.

## Función en el procesamiento de textos

La tokenización sirve varias funciones esenciales en el procesamiento de textos:

**Preprocesamiento:** Simplifica el texto para el análisis, eliminando la complejidad de trabajar con una secuencia continua de caracteres.

**Normalización:** Permite la aplicación de técnicas de normalización como la lematización y el stemming.

**Análisis sintáctico y semántico:** Facilita el análisis gramatical y la comprensión del significado del texto al proporcionar unidades discretas de análisis.

## Métodos de tokenización

Existen varios métodos para realizar la tokenización, cada uno adecuado para diferentes tipos de aplicaciones y lenguajes:

**Tokenización basada en espacios:** Divide el texto utilizando los espacios en blanco como delimitadores. Es simple y rápida, pero puede ser ineficaz para lenguajes sin espacios claros entre palabras, como el chino.

**Tokenización basada en reglas:** Utiliza reglas predefinidas, como puntuación y espacios, para segmentar el texto. Este método puede ser ajustado para manejar contracciones y otros casos especiales.

**Tokenización basada en aprendizaje automático:** Utiliza modelos entrenados para identificar los límites de los tokens. Es más flexible y puede manejar casos complejos, pero requiere más recursos computacionales y datos de entrenamiento.

## Aplicaciones prácticas

La tokenización se utiliza en una amplia gama de aplicaciones de NLP, tales como:

**Análisis de sentimientos:** Identificar y clasificar opiniones en el texto.
**Clasificación de texto:** Asignar categorías a documentos basados en su contenido.
**Traducción automática:** Dividir el texto en unidades que pueden ser traducidas individualmente.
**Extracción de información:** Identificar entidades y relaciones clave dentro del texto.

### Ejemplo de código en Python

A continuación, se muestra un ejemplo de tokenización utilizando la biblioteca NLTK en Python:

```python
# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize

# Descargar 'punkt' solo si no está disponible
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

texto = "El procesamiento de lenguaje natural es todo un mundo."
tokens = word_tokenize(texto)

print(tokens)

```
Este código divide la frase en palabras individuales utilizando la biblioteca NLTK, una de las herramientas más populares para el procesamiento de lenguaje natural en Python.

La tokenización es un paso esencial en el procesamiento de texto en **NLP**, ya que prepara el texto para un análisis más profundo y detallado. Sin una tokenización adecuada, otras técnicas de NLP no podrían aplicarse de manera efectiva.

## Lematización y stemming

La lematización y el stemming son técnicas fundamentales en el Procesamiento de Lenguaje Natural (NLP) utilizadas para reducir las palabras a sus formas base o raíz. Estas técnicas son esenciales para normalizar el texto y mejorar la precisión de los análisis posteriores.

### Qué es la lematización

La **lematización** es el proceso de reducir una palabra a su forma base o “lema”, que es su forma canónica en el diccionario. Este proceso considera el contexto y las reglas gramaticales para convertir diferentes formas de una palabra en su forma raíz.

**Ejemplo:** Las palabras “corriendo”, “corre” y “corrí” se lematizan a “correr”.

La lematización es más precisa que el stemming porque tiene en cuenta el contexto y el significado de las palabras. Utiliza un diccionario de palabras y una comprensión de la estructura gramatical para hacer la conversión correcta.

### Qué es el stemming

El **stemming** es una técnica más sencilla que corta los sufijos de las palabras para reducirlas a su **raíz morfológica**. A diferencia de la lematización, el stemming no necesariamente produce palabras con significado, sino simplemente la forma troncal de las palabras.

**Ejemplo:** Las palabras “corriendo”, “corre” y “corrí” se reducen a “corr”.

El stemming es más rápido y menos complejo que la lematización, pero también puede ser menos preciso porque no considera el contexto gramatical.

## Algoritmos utilizados

**Algoritmo de Porter:** Es uno de los algoritmos de stemming más utilizados y fue desarrollado por Martin Porter en 1980. Este algoritmo aplica una serie de reglas para cortar los sufijos y obtener la raíz de la palabra.

```python
# -*- coding: utf-8 -*-
from nltk.stem import PorterStemmer

ps = PorterStemmer()
palabras = ["corriendo", "corre", "corrí"]
for palabra in palabras:
    print(ps.stem(palabra))
```

**Algoritmo de Snowball:** Es una versión mejorada del algoritmo de Porter y soporta múltiples idiomas.
```python
# -*- coding: utf-8 -*-
from nltk.stem import SnowballStemmer

ss = SnowballStemmer("spanish")
palabras = ["corriendo", "corre", "corrí"]
for palabra in palabras:
    print(ss.stem(palabra))
```

**Lematización con WordNet:** Utiliza el diccionario de WordNet para realizar la lematización en inglés.

```python
# -*- coding: utf-8 -*-
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Descargar recursos de WordNet solo si no están disponibles
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4')

# crea el lematizador y define palabras en español
lemmatizer = WordNetLemmatizer()
palabras = ["corriendo", "corre", "corrí"]

# Lematiza cada palabra como verbo
for palabra in palabras:
    print(lemmatizer.lemmatize(palabra, pos=wordnet.VERB))

```
## Casos de uso

**Búsqueda y recuperación de información:** La lematización y el stemming son utilizados para mejorar la precisión en motores de búsqueda al tratar diferentes formas de una palabra como equivalentes.

**Análisis de sentimientos:** Estas técnicas ayudan a normalizar el texto para identificar sentimientos y opiniones con mayor precisión.

**Clasificación de texto:** Al reducir las palabras a sus formas base, se mejora la consistencia y precisión en la clasificación de documentos.

Ambas técnicas son cruciales en el procesamiento de texto, y la elección entre lematización y stemming depende de los requisitos específicos de la aplicación y la necesidad de precisión versus eficiencia.

# Eliminación de stop words

La eliminación de stop words es una técnica común en el Procesamiento de Lenguaje Natural (NLP) que implica la eliminación de palabras muy frecuentes en un idioma que no aportan un significado relevante al análisis del texto.

Estas palabras incluyen artículos, preposiciones, pronombres y conjunciones, como “el”, “la”, “de”, “y”, “pero”, entre otras.

## Qué son las stop words

Las stop words son palabras que, aunque son esenciales para la construcción gramatical de las oraciones, no aportan un contenido significativo que ayude en tareas de análisis como la clasificación de texto, la extracción de información o el análisis de sentimientos. Su detección y eliminación ayuda a reducir el ruido en el texto y a enfocar el análisis en las palabras más importantes.

## Importancia de las stop words

La eliminación de stop words es crucial por varias razones:

**Reducción de Ruido:** Ayuda a eliminar palabras que no contribuyen significativamente al contenido del texto, reduciendo el ruido y mejorando la precisión de los algoritmos de NLP.

**Eficiencia Computacional:** Disminuye el tamaño del texto a procesar, lo que mejora la velocidad y eficiencia de los algoritmos de procesamiento de texto.

**Mejora de Resultados:** Al enfocar el análisis en palabras más relevantes, se mejoran los resultados de tareas como la clasificación de documentos, la extracción de entidades y el análisis de sentimientos.

## Técnicas de eliminación

**Listas predefinidas de stop words:** La manera más común de eliminar stop words es utilizar listas predefinidas que contienen las palabras más comunes en un idioma específico. Estas listas están disponibles en muchas bibliotecas de NLP, como NLTK y spaCy.

```python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Descargar recursos de NLTK si no están disponibles
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Define el texto y obtiene las stopwords en español
texto = "El procesamiento de lenguaje natural es todo un mundo y útil en muchas aplicaciones."
# stopwords en español
stop_words = set(stopwords.words('spanish'))
# Tokenizar el texto y filtrar las palabras vacias
palabras = word_tokenize(texto)
palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words]
print(palabras_filtradas)
```

**Eliminación basada en frecuencia:** Otra técnica es eliminar palabras que aparecen con una frecuencia extremadamente alta en un corpus específico. Esto se puede hacer calculando la frecuencia de las palabras y eliminando las más comunes.

```python
# -*- coding: utf-8 -*-

from collections import Counter
from nltk.tokenize import word_tokenize

texto = "El procesamiento de lenguaje natural es todo un mundo y útil en muchas aplicaciones. El lenguaje natural permite la comunicación."

palabras = word_tokenize(texto)
frecuencia = Counter(palabras)

palabras_filtradas = [palabra for palabra in palabras if frecuencia[palabra] < 3]
print(palabras_filtradas)
```

## Impacto en el procesamiento de texto

**Mejora en la clasificación de textos:** La eliminación de stop words puede aumentar la precisión en la clasificación de textos al reducir el ruido y centrar el análisis en las palabras más relevantes.

**Optimización de motores de búsqueda:** Ayuda a mejorar la relevancia de los resultados de búsqueda al ignorar palabras comunes que no aportan valor informativo.

**Análisis de sentimientos y opiniones:** Facilita la identificación de palabras clave y emociones en el texto, proporcionando resultados más precisos y útiles.

La eliminación de stop words es una práctica estándar en el procesamiento de texto que ayuda a mejorar la calidad y eficiencia de muchas aplicaciones de NLP.

# TF-IDF (Term Frequency-Inverse Document Frequency)

TF-IDF, que significa “Term Frequency-Inverse Document Frequency”, es una técnica ampliamente utilizada en el Procesamiento de Lenguaje Natural (NLP) para evaluar la importancia de una palabra en un documento en relación con un corpus de documentos.

Este método ayuda a identificar qué palabras son más relevantes en un texto específico, permitiendo una mejor comprensión y análisis de datos textuales.

## Qué es TF-IDF

TF-IDF combina dos métricas diferentes:

**Term Frequency (TF):** Mide la frecuencia de una palabra en un documento específico. La fórmula básica es:

![TF](tecnicas1.webp)

**Inverse Document Frequency (IDF):** Mide la importancia de una palabra en todo el corpus, considerando cuántos documentos contienen la palabra. La fórmula básica es:

![IDF](tecnicas2.webp)

El valor de TF-IDF se obtiene multiplicando TF y IDF:

![TF-IDF](tecnicas3.webp)

## Importancia de TF-IDF

TF-IDF es crucial porque permite identificar términos que son relevantes en un documento particular mientras se descartan palabras comunes que aparecen en muchos documentos (stop words). Esto es especialmente útil en tareas como la clasificación de textos, la búsqueda de información y la minería de textos.

## Proceso de cálculo

**Cálculo de TF:** Se calcula la frecuencia de cada término en el documento.

**Cálculo de IDF:** Se calcula la frecuencia inversa de documentos para cada término en el corpus.

**Multiplicación de TF e IDF:** Se multiplica el valor de TF por el valor de IDF para obtener el puntaje TF-IDF de cada término en el documento.

## Aplicaciones y ejemplos

**Clasificación de Texto:** TF-IDF se utiliza para convertir documentos en vectores de características que luego pueden ser utilizados por algoritmos de aprendizaje automático para la clasificación.

**Búsqueda de Información:** Mejora la relevancia de los resultados de búsqueda al dar mayor peso a términos que son más significativos en el contexto del documento consultado.

**Análisis de Contenido:** Ayuda a identificar palabras clave y temas predominantes en grandes colecciones de textos.

### Ejemplo de código en Python

A continuación, se muestra un ejemplo de cómo calcular TF-IDF utilizando la biblioteca scikit-learn en Python:

ejemplo: **ifsceikit.py**

```python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer

# Documentos de ejemplo
documentos = [
    "El procesamiento de lenguaje natural es todo un mundo.",
    "El lenguaje natural permite la comunicación entre humanos y máquinas.",
    "Las técnicas de NLP mejoran la comprensión del texto."
]

# Crear el vectorizador TF-IDF
vectorizer = TfidfVectorizer()

# Calcular la matriz TF-IDF
tfidf_matrix = vectorizer.fit_transform(documentos)

# Mostrar la matriz TF-IDF
print(tfidf_matrix.toarray())

# Mostrar los términos
print(vectorizer.get_feature_names_out())

```

Este código transforma una lista de documentos en una matriz TF-IDF, donde cada fila representa un documento y cada columna representa un término, con valores que indican la importancia de cada término en cada documento.

TF-IDF es una técnica poderosa y versátil en el procesamiento de texto, que ayuda a mejorar la precisión y relevancia en una variedad de aplicaciones de NLP.

# Word embeddings

Los word embeddings son una técnica avanzada en el Procesamiento de Lenguaje Natural (NLP) que permite representar palabras en un espacio vectorial continuo.

A diferencia de las representaciones tradicionales basadas en frecuencias, los word embeddings capturan el significado semántico de las palabras al modelar sus contextos de uso.

Esto se logra mediante el aprendizaje de representaciones de alta dimensión que posicionan palabras con significados similares cerca unas de otras en el espacio vectorial.

## Qué son los word embeddings

Los word embeddings son vectores densos y de baja dimensión que representan palabras de manera que palabras con significados similares tengan representaciones vectoriales cercanas.

Esta técnica se basa en la idea de que las palabras que aparecen en contextos similares tienden a tener significados relacionados.

**Ejemplo:** En un modelo de word embeddings, las palabras “rey” y “reina” estarían representadas por vectores que están cerca entre sí en el espacio vectorial, debido a su relación semántica.

## Importancia de los word embeddings

Los word embeddings son fundamentales en NLP porque:

**Capturan relaciones semánticas:** Permiten que las máquinas comprendan relaciones semánticas y sintácticas complejas entre palabras.

**Reducción de dimensionalidad:** Reducen la dimensionalidad del espacio de características, haciendo que los modelos sean más eficientes y manejables.

**Generalización:** Mejoran la capacidad de los modelos para generalizar a nuevos datos al capturar patrones y relaciones inherentes en el lenguaje.

## Modelos populares de word embeddings

**Word2Vec:** Desarrollado por Google, Word2Vec utiliza dos arquitecturas principales (CBOW y Skip-Gram) para aprender representaciones vectoriales de palabras.

CBOW predice una palabra a partir de su contexto, mientras que Skip-Gram predice el contexto a partir de una palabra.

ejemplo: **w2v.py**

```python
# -*- coding: utf-8 -*-
import gensim
from gensim.models import Word2Vec

# Ejemplo de uso de Word2Vec
sentences = [["el", "procesamiento", "de", "lenguaje", "natural", "es", "todo", "un", "mundo"],
             ["el", "lenguaje", "natural", "permite", "la", "comunicación", "entre", "humanos", "y", "máquinas"]]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
vector = model.wv['lenguaje']
print(vector)

```
**GloVe (Global Vectors for Word Representation):** Desarrollado por Stanford, GloVe combina la eficiencia de la matriz de co-ocurrencia con la precisión de los modelos de embeddings.

Captura relaciones semánticas mediante el modelado de las co-ocurrencias globales de palabras en un corpus.

ejemplo: **glomix.py**
```python
# -*- coding: utf-8 -*-
# GloVe no tiene una implementación directa en Python, pero los vectores preentrenados están disponibles para su uso.
import numpy as np

# Cargar los vectores GloVe preentrenados (suponiendo que se han descargado)
def load_glove_model(file_path):
    glove_model = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            split_line = line.split()
            word = split_line[0]
            vector = np.array(split_line[1:], dtype=float)
            glove_model[word] = vector
    return glove_model

glove_model = load_glove_model('glove.6B.100d.txt')
print(glove_model['lenguaje'])
```

**FastText:** Desarrollado por Facebook, FastText extiende Word2Vec al considerar subpalabras o n-gramas. Esto permite que el modelo maneje mejor palabras raras y fuera de vocabulario (OOV).

ejemplo: **voox.py**

```python
# -*- coding: utf-8 -*-

from gensim.models import FastText

# Ejemplo de uso de FastText
sentences = [["el", "procesamiento", "de", "lenguaje", "natural", "es", "todo", "un", "mundo"],
             ["el", "lenguaje", "natural", "permite", "la", "comunicación", "entre", "humanos", "y", "máquinas"]]
model = FastText(sentences, vector_size=100, window=5, min_count=1, workers=4)
vector = model.wv['lenguaje']
print(vector)

```

## Aplicaciones en el procesamiento de texto

**Clasificación de textos:** Los word embeddings son utilizados para transformar textos en vectores de características que luego son clasificados mediante algoritmos de aprendizaje automático.

**Análisis de sentimientos:** Permiten identificar y clasificar emociones en textos al mapear palabras a vectores que reflejan su carga semántica.

**Sistemas de recomendación:** Utilizan embeddings para entender mejor las preferencias de los usuarios y ofrecer recomendaciones personalizadas.

Los word embeddings han revolucionado el procesamiento de texto en NLP al proporcionar una forma efectiva y eficiente de representar el significado de las palabras.

Su capacidad para capturar relaciones semánticas complejas ha mejorado significativamente el rendimiento de muchos sistemas de NLP.

# N-gramas


Los N-gramas son secuencias contiguas de ‘n’ elementos de un texto o discurso, donde los elementos pueden ser caracteres, sílabas, palabras o incluso frases.

En el campo del Procesamiento de Lenguaje Natural (NLP), los N-gramas son herramientas fundamentales que se utilizan para modelar el contexto y la estructura de un texto, permitiendo una comprensión más profunda y precisa del lenguaje.

## Aplicaciones en el procesamiento de texto

Los N-gramas se aplican en diversas tareas de NLP, entre las que se incluyen:

Modelado del lenguaje: Los modelos de N-gramas predicen la probabilidad de una palabra basándose en las ‘n-1’ palabras anteriores, ayudando a generar texto coherente y fluido.

**Clasificación de texto:** Utilizados como características en algoritmos de clasificación para identificar el tema o la categoría de un documento.

**Corrección ortográfica:** Ayudan a identificar y corregir errores basándose en la probabilidad de secuencias de caracteres o palabras.

**Análisis de sentimientos:** Permiten capturar contextos locales de sentimientos o emociones en un texto, mejorando la precisión del análisis.

**Sistemas de recomendación:** Utilizan patrones de N-gramas para predecir el siguiente ítem o palabra que un usuario podría buscar o necesitar.

## Tipos de n-gramas

**Unigramas:** Son N-gramas donde ‘n’ es igual a 1. Representan palabras individuales en el texto.

**Bigramas:** Son N-gramas donde ‘n’ es igual a 2. Representan pares de palabras consecutivas.

**Trigramas:** Son N-gramas donde ‘n’ es igual a 3. Representan secuencias de tres palabras consecutivas.

La elección del valor de ‘n’ depende de la aplicación específica y del equilibrio entre complejidad y capacidad de capturar contexto.

## Generación de n-gramas

La generación de N-gramas implica dividir un texto en secuencias de longitud ‘n’. A continuación se muestra un ejemplo en Python utilizando la biblioteca nltk:

ejemplo: **ngram.py**

```python
# -*- coding: utf-8 -*-
import nltk
from nltk.util import ngrams
from collections import Counter

# Descargar los datos necesarios de NLTK
nltk.download('punkt')

# Texto de ejemplo
texto = "El procesamiento de lenguaje natural es fascinante y útil en muchas aplicaciones."

# Tokenizar el texto
tokens = nltk.word_tokenize(texto)

# Generar bigramas
bigrams = list(ngrams(tokens, 2))

# Contar la frecuencia de los bigramas
bigram_freq = Counter(bigrams)

print(bigrams)
print(bigram_freq)
```

## Aplicaciones prácticas

**Modelado del lenguaje:** Los modelos de N-gramas se utilizan en sistemas de reconocimiento de voz, predicción de texto y generación automática de texto.

Por ejemplo, un modelo de bigramas puede predecir la siguiente palabra en una secuencia basándose en la palabra anterior.

**Clasificación de texto:** Los N-gramas pueden ser utilizados como características en modelos de clasificación para determinar la categoría o el tema de un texto.

Por ejemplo, un clasificador de spam puede utilizar bigramas y trigramas para identificar patrones comunes en correos electrónicos no deseados.

**Análisis de sentimientos:** Los N-gramas ayudan a identificar secuencias de palabras que expresan sentimientos o emociones, mejorando la precisión en el análisis de opiniones en redes sociales y reseñas de productos.

**Corrección ortográfica:** Los sistemas de corrección ortográfica pueden utilizar N-gramas para sugerir correcciones basadas en las secuencias más probables de letras o palabras.

Los N-gramas son una herramienta poderosa y flexible en el procesamiento de texto, permitiendo capturar contextos y patrones que mejoran el rendimiento de diversos sistemas y aplicaciones de NLP.

# Reconocimiento de entidades nombradas (NER)

El Reconocimiento de Entidades Nombradas (NER, por sus siglas en inglés) es una técnica crucial en el Procesamiento de Lenguaje Natural (NLP) que implica la identificación y clasificación de entidades mencionadas en un texto.

Estas entidades pueden incluir nombres de personas, organizaciones, lugares, fechas, cantidades y otras categorías predefinidas. El objetivo de NER es estructurar y extraer información relevante de textos no estructurados, facilitando el análisis y la búsqueda de datos.

## Qué es NER

NER es el proceso de detectar y etiquetar automáticamente las entidades nombradas dentro de un texto. Por ejemplo, en la oración “Apple lanzó el nuevo iPhone en California el 13 de octubre”, NER identificaría “Apple” como una organización, “iPhone” como un producto, “California” como un lugar y “13 de octubre” como una fecha.

## Técnicas y algoritmos

Existen varias técnicas y algoritmos para implementar NER, que van desde enfoques basados en reglas hasta métodos avanzados de aprendizaje automático y aprendizaje profundo.

**Enfoques basados en reglas:** Utilizan patrones y expresiones regulares para identificar entidades. Estos métodos son simples, pero pueden ser limitados en su capacidad para manejar variabilidad en el texto.

ejemplo: **near.py**

```python
# -*- coding: utf-8 -*-
import re

texto = "Apple lanzó el nuevo iPhone en California el 13 de octubre"
patrones = {
    "ORGANIZACION": r"\bApple\b",
    "PRODUCTO": r"\biPhone\b",
    "LUGAR": r"\bCalifornia\b",
    "FECHA": r"\b13 de octubre\b"
}

for entidad, patron in patrones.items():
    if re.search(patron, texto):
        print(f"{entidad}: {re.search(patron, texto).group()}")
```
**Modelos basados en aprendizaje automático:** Utilizan algoritmos de clasificación supervisada, como Support Vector Machines (SVM) y Conditional Random Fields (CRF), para etiquetar entidades. Estos modelos requieren un corpus anotado para el entrenamiento.

**Modelos de aprendizaje profundo:** Utilizan redes neuronales, como redes neuronales recurrentes (RNN) y transformers, para realizar NER con alta precisión. Modelos preentrenados como BERT y SpaCy son populares en esta categoría.

ejemplo: **modapre.py**

```py
# -*- coding: utf-8 -*-
import spacy

# Cargar el modelo preentrenado de SpaCy
nlp = spacy.load("es_core_news_sm")

texto = "Apple lanzó el nuevo iPhone en California el 13 de octubre"
doc = nlp(texto)

for entidad in doc.ents:
    print(entidad.text, entidad.label_)

```
previamente: 
    `python -m spacy download es_core_news_md`
    `python -m spacy download es_core_news_sm`

# Aplicaciones prácticas

NER tiene una amplia variedad de aplicaciones en diferentes dominios:

Análisis de texto en medios de comunicación: Automatiza la extracción de nombres de personas, lugares y organizaciones de artículos de noticias, facilitando el análisis y la búsqueda de información.

**Atención al cliente:** Mejora los chatbots y asistentes virtuales al permitirles identificar y manejar entidades mencionadas por los usuarios.

**Gestión de información médica:** Extrae entidades como nombres de medicamentos, enfermedades y procedimientos de registros médicos electrónicos para mejorar la gestión y análisis de datos de salud.

**Finanzas y negocios:** Identifica nombres de empresas, valores, fechas y otros datos relevantes en informes financieros y noticias de mercado.

## Ejemplo de código en Python con SpaCy

A continuación, se muestra un ejemplo de cómo utilizar SpaCy para realizar NER:

ejemplo: **nercy.py**

```py
# -*- coding: utf-8 -*-
import spacy

# Cargar el modelo preentrenado de SpaCy
try:
    nlp = spacy.load("es_core_news_sm")
except OSError:
    import os
    os.system("python -m spacy download es_core_news_sm")

# nlp = spacy.load("es_core_news_sm")

texto = "Apple lanzó el nuevo iPhone en California el 13 de octubre"

doc = nlp(texto)

for entidad in doc.ents:
    print(entidad.text, entidad.label_)
```

Este código carga un modelo preentrenado de SpaCy para el idioma español y aplica NER al texto de ejemplo, identificando y etiquetando entidades nombradas.

El Reconocimiento de Entidades Nombradas es una técnica poderosa y versátil en el procesamiento de texto que facilita la estructuración y análisis de grandes volúmenes de datos textuales, proporcionando valor significativo en múltiples aplicaciones y dominios.

# Análisis de sentimientos

El análisis de sentimientos es una técnica clave en el Procesamiento de Lenguaje Natural (NLP) que implica determinar las emociones, opiniones y actitudes expresadas en un texto.

Esta técnica es ampliamente utilizada en diversas aplicaciones, desde la monitorización de redes sociales hasta la satisfacción del cliente, permitiendo a las organizaciones entender mejor las percepciones y reacciones de las personas.

## Qué es el análisis de sentimientos

El análisis de sentimientos, también conocido como minería de opiniones, se enfoca en identificar y extraer información subjetiva de los textos.

El objetivo es clasificar las expresiones en categorías como positivas, negativas o neutras, y en algunos casos, identificar emociones más específicas como alegría, tristeza, enojo, etc.

## Propósito del análisis de sentimientos

El análisis de sentimientos es esencial para varias razones:

**Entender las opiniones del cliente:** Ayuda a las empresas a analizar reseñas de productos, comentarios en redes sociales y encuestas para evaluar la satisfacción del cliente y mejorar sus productos y servicios.

**Monitorización de marca:** Permite a las empresas monitorear cómo se percibe su marca en el mercado y reaccionar a tiempo ante crisis de relaciones públicas.

**Análisis de competencia:** Combinado con técnicas de Machine Learning (ML), facilita el seguimiento de las opiniones sobre los competidores y las tendencias del mercado.

## Técnicas y modelos

Existen varias técnicas y modelos utilizados en el análisis de sentimientos, que van desde enfoques basados en reglas hasta métodos avanzados de aprendizaje automático y aprendizaje profundo.

**Enfoques basados en reglas:** Utilizan diccionarios de palabras con etiquetas de sentimientos (positivas, negativas, neutras) y reglas gramaticales para identificar el sentimiento. Este método es simple, pero puede no capturar matices complejos del lenguaje.

propiedad: **enfoque.py**

```py
# -*- coding: utf-8 -*-
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Descargar los datos necesarios de NLTK
nltk.download('vader_lexicon')

texto = "Me encanta el nuevo iPhone, es increíble."
sid = SentimentIntensityAnalyzer()
scores = sid.polarity_scores(texto)
print(scores)
```
**Modelos de aprendizaje automático:** Utilizan algoritmos supervisados como Naive Bayes, Support Vector Machines (SVM) y Random Forests entrenados en datos etiquetados para clasificar el sentimiento. Requieren un corpus grande de texto etiquetado para el entrenamiento.

**Modelos de aprendizaje profundo:** Utilizan redes neuronales, como redes neuronales recurrentes (RNN) y transformers, para realizar el análisis de sentimientos con mayor precisión. Modelos preentrenados como BERT y RoBERTa son populares en esta categoría.

ejemplo: **aprex.py**

```py
# -*- coding: utf-8 -*-
from transformers import pipeline

# Cargar el modelo preentrenado de Transformers
clasificador = pipeline("sentiment-analysis")

texto = "Me encanta el nuevo iPhone, es increíble."
resultado = clasificador(texto)
print(resultado)
```

# Aplicaciones prácticas

El análisis de sentimientos tiene aplicaciones en numerosos campos:

**Redes sociales:** Analiza los comentarios y publicaciones en plataformas como Twitter y Facebook para evaluar la percepción pública sobre temas específicos, productos o eventos.

**Atención al cliente:** Procesa retroalimentación de los clientes para identificar áreas de mejora y medir la satisfacción del cliente.

**Marketing y publicidad:** Ayuda a diseñar campañas publicitarias más efectivas al comprender mejor las reacciones del público objetivo.

**Análisis político:** Evalúa las opiniones públicas sobre políticas, partidos y candidatos, proporcionando información valiosa durante las campañas electorales.

# Ejemplo de código en Python con VADER

A continuación, se muestra un ejemplo de cómo utilizar VADER (Valence Aware Dictionary and sEntiment Reasoner), una herramienta de NLTK, para realizar análisis de sentimientos:

ejemplo: **vax.py**

```py
# -*- coding: utf-8 -*-

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar los datos necesarios de NLTK
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

texto = "Me encanta el nuevo iPhone, es increíble."

sid = SentimentIntensityAnalyzer()
scores = sid.polarity_scores(texto)

print(scores)

```

Este código analiza el sentimiento del texto de ejemplo y devuelve un diccionario con puntuaciones para sentimientos positivos, negativos, neutrales y una puntuación compuesta general.

El análisis de sentimientos es una técnica poderosa que proporciona insights valiosos sobre las emociones y opiniones expresadas en grandes volúmenes de datos textuales, ayudando a las organizaciones a tomar decisiones informadas y estratégicas.

# Lo que deberías recordar de las técnicas para el procesamiento de texto en NLP

**Tokenización:** Este proceso divide el texto en unidades más pequeñas llamadas tokens, lo que facilita el análisis y procesamiento posterior.

**Lematización y stemming:** Estas técnicas reducen las palabras a sus formas base o raíz, mejorando la precisión en la búsqueda de información y análisis de texto.

**Eliminación de stop words:** Ayuda a eliminar palabras comunes que no aportan un significado significativo, reduciendo el ruido y mejorando la relevancia del análisis.

**TF-IDF:** Evalúa la importancia de una palabra en un documento en relación con un corpus, mejorando la clasificación y recuperación de información.

**Word embeddings:** Proporcionan representaciones vectoriales densas de palabras, capturando relaciones semánticas y mejorando el rendimiento de modelos de aprendizaje automático.

**N-gramas:** Capturan secuencias de ‘n’ elementos contiguos en el texto, útiles para modelar el contexto y la estructura del lenguaje.

**Reconocimiento de entidades nombradas (NER):** Identifica y clasifica entidades mencionadas en el texto, estructurando la información y facilitando la extracción de datos relevantes.

**Análisis de sentimientos:** Determina las emociones y opiniones expresadas en el texto, proporcionando insights valiosos para la toma de decisiones en diversas aplicaciones.


__________________________________________________________________

# Glove

Puedes conseguir el archivo glove.6B.100d.txt, que forma parte del conjunto de vectores preentrenados GloVe (Global Vectors for Word Representation), desde varias fuentes confiables. Aquí te dejo las mejores opciones:

Opciones para descargar glove.6B.100d.txt


| Fuente	|  Descripción  |	Enlace |
|------------|--------------|---------------|
| Sitio oficial de GloVe (Stanford)	| Incluye todos los vectores GloVe en diferentes dimensiones (50d, 100d, 200d, 300d). |	[ nlp.stanford.edu/projects/glove](https://nlp.stanford.edu/projects/glove/) |
| GitHub (tsajed/data)	| Archivo individual alojado en un repositorio público. | 	[Ver en GitHub](https://github.com/tsajed/data/blob/master/glove.6B.100d.txt) |
| Hugging Face Datasets	| Versión comprimida (.gz) del archivo, ideal para proyectos con Git LFS. |	[Descargar desde Hugging Face](https://huggingface.co/datasets/SLU-CSCI4750/glove.6B.100d.txt/blob/main/glove.6B.100d.txt.gz) |
| Kaggle Dataset	| Dataset completo disponible para usuarios registrados.	|  [Ver en Kaggle](https://www.kaggle.com/datasets/danielwillgeorge/glove6b100dtxt)  |


## ¿Cómo usarlo?

Una vez descargado, puedes cargarlo en Python así:

```python
def cargar_glove(path):
    embeddings = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            valores = line.split()
            palabra = valores[0]
            vector = list(map(float, valores[1:]))
            embeddings[palabra] = vector
    return embeddings

glove_path = "glove.6B.100d.txt"
glove_embeddings = cargar_glove(glove_path)
```
¿Quieres que te ayude a integrarlo en tu chatbot para mejorar la similitud semántica con GloVe en lugar de spaCy? También podemos combinar ambos enfoques si lo deseas.


__________________________________________________________________

# Entrenar tu propio Word2Vec en español con Gensim

Primero asegúrate de instalar gensim y nltk:

`pip install gensim nltk`

Ejemplo simple en Python:
```py
from gensim.models import Word2Vec
import nltk

# Descargar tokenizer de oraciones y palabras
nltk.download("punkt")

# Corpus pequeño en español (ejemplo)
texto = """
El aprendizaje automático es una rama de la inteligencia artificial.
El procesamiento de lenguaje natural permite a las máquinas entender el idioma humano.
Python es un lenguaje muy usado en ciencia de datos.
"""

# Tokenizar el texto en oraciones y palabras
oraciones = nltk.sent_tokenize(texto, language="spanish")
tokens = [nltk.word_tokenize(oracion, language="spanish") for oracion in oraciones]

# Entrenar modelo Word2Vec
model = Word2Vec(sentences=tokens, vector_size=100, window=5, min_count=1, workers=4)

# Ejemplo: vector de la palabra "lenguaje"
print("Vector de 'lenguaje':\n", model.wv["lenguaje"])

# Palabras más similares a "inteligencia"
print("Similares a 'inteligencia':\n", model.wv.most_similar("inteligencia"))
```

Esto entrenará un modelo muy pequeño (solo con tu texto de ejemplo).

En un proyecto real deberías usar un corpus grande en español (por ejemplo Wikipedia en español o noticias).

## Usar un modelo Word2Vec preentrenado en español

Ya existen embeddings en español entrenados en grandes corpus. Algunos recursos útiles:

    Spanish Billion Word Embeddings: https://crscardellino.github.io/SBWCE/

    FastText embeddings de Facebook (tienen español): https://fasttext.cc/docs/en/crawl-vectors.html

## Cargar un modelo preentrenado con Gensim

**Ejemplo con FastText en español:**

```py
from gensim.models import KeyedVectors

# Cargar embeddings preentrenados (ejemplo FastText español)
model = KeyedVectors.load_word2vec_format("cc.es.300.vec.gz", binary=False)

# Palabras similares
print(model.most_similar("fútbol"))
print(model.most_similar("mujer"))

```

**Nota:** Los modelos preentrenados suelen pesar varios GB, así que necesitas espacio y buena RAM.

## Con esto puedes elegir entre:

Entrenar tu propio modelo (más ligero, pero limitado).

Usar un modelo preentrenado (más poderoso, pero pesado).

¿Quieres que te prepare un ejemplo práctico de cómo descargar automáticamente el modelo FastText en español y usarlo con Gensim, o prefieres empezar con un entrenamiento casero sobre un corpus pequeño que ya tengas?