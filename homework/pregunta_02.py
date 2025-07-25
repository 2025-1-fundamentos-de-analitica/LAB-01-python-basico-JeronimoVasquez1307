"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os
def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    ruta = "files/input/data.csv"
    letras = {}
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as archivo:

            for linea in archivo:
                line = linea.strip().split()
                if line[0] in letras:
                    letras[linea[0]] += 1
                else:
                    letras[linea[0]] = 1
        
        tuplas = sorted([(letra,cantidad) for letra, cantidad in letras.items()])
        return tuplas
    else:
        print("La ruta no existe")

    

print(pregunta_02())