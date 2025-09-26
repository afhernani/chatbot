# -*- coding: utf-8 -*-
import spacy

# Cargar el modelo preentrenado de SpaCy
nlp = spacy.load("es_core_news_sm")

texto = "Apple lanzó el nuevo iPhone en California el 13 de octubre"
doc = nlp(texto)

for entidad in doc.ents:
    print(entidad.text, entidad.label_)
