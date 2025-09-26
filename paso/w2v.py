# -*- coding: utf-8 -*-
import gensim
from gensim.models import Word2Vec

# Ejemplo de uso de Word2Vec
sentences = [["el", "procesamiento", "de", "lenguaje", "natural", "es", "todo", "un", "mundo"],
             ["el", "lenguaje", "natural", "permite", "la", "comunicación", "entre", "humanos", "y", "máquinas"]]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
vector = model.wv['lenguaje']
print(vector)