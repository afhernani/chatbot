# -*- coding: utf-8 -*-
# pip install nltk scikit-learn

import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
