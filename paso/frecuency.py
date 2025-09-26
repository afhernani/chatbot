# -*- coding: utf-8 -*-

from collections import Counter
from nltk.tokenize import word_tokenize

texto = "El procesamiento de lenguaje natural es todo un mundo y útil en muchas aplicaciones. El lenguaje natural permite la comunicación."

palabras = word_tokenize(texto)
frecuencia = Counter(palabras)

palabras_filtradas = [palabra for palabra in palabras if frecuencia[palabra] < 3]
print(palabras_filtradas)