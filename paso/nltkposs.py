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