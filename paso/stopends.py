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