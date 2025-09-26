# -*- coding: utf-8 -*-

import nltk
from nltk import word_tokenize, pos_tag
# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
# Sample text
text = "NLTK is a poerful library for natural language processing."
# Perform POS tagging
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
# pos_tags = nltk.pos_tag(nltk.word_tokenize(text))
# Display the POS tags
print(tags)
