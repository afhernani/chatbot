# -*- coding: utf-8 -*-

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar los datos necesarios de NLTK
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

texto = "Me encanta el nuevo iPhone, es increíble."

sid = SentimentIntensityAnalyzer()

scores = sid.polarity_scores(texto)

print(scores)