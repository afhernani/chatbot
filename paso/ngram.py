# -*- coding: utf-8 -*-
import nltk
from nltk.util import ngrams
from collections import Counter

# Descargar los datos necesarios de NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
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