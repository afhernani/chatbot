# -*- coding: utf-8 -*-

from nltk.stem import SnowballStemmer

ss = SnowballStemmer("spanish")

palabras = ["corriendo", "corre", "corrí"]

for palabra in palabras:
    print(ss.stem(palabra))