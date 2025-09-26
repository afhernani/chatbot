# -*- coding: utf-8 -*-

from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("spanish")

palabras = ["corriendo", "corre", "corrí"]

for palabra in palabras:
    print(stemmer.stem(palabra))