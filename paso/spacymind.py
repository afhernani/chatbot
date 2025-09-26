# -*- coding: utf-8 -*-

import spacy
# Load the spacy modl for the English language
nlp = spacy.load("es_core_news_md")
# samaple text to be tokenized
text = "Spacy is a powerfull python library for natural language processing"
# Process the text using spacy
doc = nlp(text)
#Tokenize the text an print each token
for token in doc:
    print(token.text)

