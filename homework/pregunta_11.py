"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    ruta = "files/input/data.csv"
    letras = {}
    if os.path.exists(ruta):

        with open(ruta, 'r', encoding= 'utf-8') as archivo:

            for linea in archivo:

                line = linea.strip().split()

                num = int(line[1])

                letras2 = line[3].split(',')

                for letra in letras2:
                    if letra in letras:
                        letras[letra] += num
                    else:
                        letras[letra] = num


            resultado = {k: letras[k] for k in sorted(letras)}

            return resultado

print(pregunta_11())

