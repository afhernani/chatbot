# -*- coding: utf-8 -*-
# GloVe no tiene una implementación directa en Python, pero los vectores 
# preentrenados están disponibles para su uso.

import numpy as np

# Cargar los vectores GloVe preentrenados (suponiendo que se han descargado)
def load_glove_model(file_path):
    glove_model = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            split_line = line.split()
            word = split_line[0]
            vector = np.array(split_line[1:], dtype=float)
            glove_model[word] = vector
    return glove_model

glove_model = load_glove_model('glove.6B.100d.txt')
print(glove_model['lenguaje'])