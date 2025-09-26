# -*- coding: utf-8 -*-

import spacy
# Load the spaCy model (English)
nlp = spacy.load("es_core_news_md")
# Sample text for POS tagging
text = "SpaCy is a popular Python library for natural language processing."
# Process the text using spaCy
doc = nlp(text)
# Print the token and its POS tag for each word in the text
for token in doc:
    print(token.text, token.pos_)
