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