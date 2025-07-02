"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    ruta = "files/input/data.csv"
    tuplas = []
    if os.path.exists(ruta):

        with open(ruta, 'r', encoding= 'utf-8') as archivo:

            for linea in archivo:
                line = linea.strip().split()

                letra = line[0]
                col4 = len(line[3].split(','))
                col5 = len(line[4].split(','))

                tupla = (letra, col4, col5)
                tuplas.append(tupla)

            return tuplas
        

print(pregunta_10())