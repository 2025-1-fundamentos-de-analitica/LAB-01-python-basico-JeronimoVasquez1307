"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    ruta = "files/input/data.csv"

    if os.path.exists(ruta):
        with open(ruta, 'r',encoding='utf-8') as archivo:

            suma = 0
            for linea in archivo:
                
                line = linea.strip().split()
                suma += int(line[1])
            
            return suma
    else:
        print("La ruta está mal")

    
    

print(pregunta_01())
