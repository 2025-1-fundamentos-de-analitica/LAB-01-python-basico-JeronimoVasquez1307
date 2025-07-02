"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    ruta = "files/input/data.csv"

    tuplas = {}
    if os.path.exists(ruta):

        with open(ruta, 'r', encoding= 'utf-8') as archivo:

            for linea in archivo:
                line = linea.strip().split()

                num = int(line[1])

                if num in tuplas:
                    tuplas[num].append(line[0])
                else:
                    tuplas[num] = [line[0]]

            
            resultado = sorted([num, letras] for num, letras in tuplas.items())
            resultados = []
            for result in resultado:
                tupla = (result[0], result[1])
                resultados.append(tupla)
            return resultados
    

print(pregunta_07())
