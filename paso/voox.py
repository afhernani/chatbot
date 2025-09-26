# -*- coding: utf-8 -*-

from gensim.models import FastText

# Ejemplo de uso de FastText
sentences = [["el", "procesamiento", "de", "lenguaje", "natural", "es", "todo", "un", "mundo"],
             ["el", "lenguaje", "natural", "permite", "la", "comunicación", "entre", "humanos", "y", "máquinas"]]

model = FastText(sentences, vector_size=100, window=5, min_count=1, workers=4)

vector = model.wv['lenguaje']

print(vector)