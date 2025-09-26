# -*- coding: utf-8 -*-
# python -m pip install transformers
# python -m pip install torch   # o tensorflow, según tu preferencia
from transformers import pipeline

# Cargar el modelo preentrenado de Transformers
clasificador = pipeline("sentiment-analysis")

texto = "Me encanta el nuevo iPhone, es increíble."
resultado = clasificador(texto)
print(resultado)