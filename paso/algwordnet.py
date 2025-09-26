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