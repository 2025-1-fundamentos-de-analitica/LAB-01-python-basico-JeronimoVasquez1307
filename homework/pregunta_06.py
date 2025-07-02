"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os   

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    ruta = "files/input/data.csv"
    grupos = {}
    if os.path.exists(ruta):

        with open(ruta, 'r', encoding= 'utf-8') as archivo:

            for linea in archivo:
                line = linea.strip().split()
                letras = line[4].split(',')

                for par in letras:
                    clave, num = par.split(":")
                    num = int(num)
                    if clave not in grupos:
                        grupos[clave] = (num, num)
                    else:
                        min_act, max_act = grupos[clave]
                        nuevo_max = max(max_act, num)
                        nuevo_min = min(min_act, num)
                        grupos[clave] = (nuevo_min, nuevo_max)

            resultado = sorted([letras, maximo, minimo] for letras, (maximo, minimo) in grupos.items())
            resultados = []
            for result in resultado:
                tupla = (result[0], result[1], result[2])
                resultados.append(tupla)
            return resultados
                

print(pregunta_06())