# -*- coding: utf-8 -*-

import re

texto = "Apple lanzó el nuevo iPhone en California el 13 de octubre"
patrones = {
    "ORGANIZACION": r"\bApple\b",
    "PRODUCTO": r"\biPhone\b",
    "LUGAR": r"\bCalifornia\b",
    "FECHA": r"\b13 de octubre\b"
}

# Buscar y mostrar las entidades encontradas
for entidad, patron in patrones.items():
    if re.search(patron, texto):
        print(f"{entidad}: {re.search(patron, texto).group()}")