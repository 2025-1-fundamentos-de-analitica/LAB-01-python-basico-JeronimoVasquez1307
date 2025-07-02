"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    ruta = "files/input/data.csv"
    letras = {}
    if os.path.exists(ruta):

        with open(ruta, 'r', encoding = 'utf-8') as archivo:

            for linea in archivo:

                line = linea.strip().split()
                letra = line[0]
                num = int(line[1])

                if letra not in letras:
                    letras[letra] = (num, num)
                
                else:
                    max_act, min_act = letras[letra]
                    nuevo_max = max(max_act, num)
                    nuevo_min = min(min_act, num)
                    letras[letra] = (nuevo_max, nuevo_min)

            resultado = sorted([letra, maximo, minimo] for letra, (maximo, minimo) in letras.items())

            resultados = []
            for result in resultado:
                tupla = (result[0], result[1], result[2])
                resultados.append(tupla)
            return resultados
    else:
        print("La ruta está mal")


print(pregunta_05())
