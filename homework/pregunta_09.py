"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

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

                    if clave not in grupos:
                        grupos[clave] = 1
                    else:
                        grupos[clave] +=1
            resultado = {k: grupos[k] for k in sorted(grupos)}
            return resultado
                

print(pregunta_09())
    
