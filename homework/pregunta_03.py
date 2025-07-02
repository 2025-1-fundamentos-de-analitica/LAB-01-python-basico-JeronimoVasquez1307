"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    ruta = "files/input/data.csv"
    letras = {}
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as archivo:

            for linea in archivo:
                line = linea.strip().split()
                if line[0] in letras:
                    letras[linea[0]] += int(line[1])
                else:
                    letras[linea[0]] = int(line[1])
        
        tuplas = sorted([(letra,cantidad) for letra, cantidad in letras.items()])
        return tuplas
    else:
        print("La ruta no existe")

print(pregunta_03())