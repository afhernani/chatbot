# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer

# Documentos de ejemplo
documentos = [
    "El procesamiento de lenguaje natural es todo un mundo.",
    "El lenguaje natural permite la comunicación entre humanos y máquinas.",
    "Las técnicas de NLP mejoran la comprensión del texto."
]

# Crear el vectorizador TF-IDF
vectorizer = TfidfVectorizer()

# Calcular la matriz TF-IDF
tfidf_matrix = vectorizer.fit_transform(documentos)

# Mostrar la matriz TF-IDF
print(tfidf_matrix.toarray())

# Mostrar los términos
print(vectorizer.get_feature_names_out())