"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    ruta = "files/input/data.csv"
    tuplas = {}
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding= 'utf-8') as archivo:

            for linea in archivo:
                line = linea.strip().split()

                num = int(line[1])
                letra = line[0]
                if num in tuplas:
                    if letra not in tuplas[num]:
                        tuplas[num].append(letra)
                else:
                    tuplas[num] = [letra]


        resultado = sorted([(num, sorted(letras)) for num, letras in tuplas.items()])

        return resultado
    

print(pregunta_08())