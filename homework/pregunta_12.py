"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    ruta = "files/input/data.csv"
    letras = {}
    if os.path.exists(ruta):

        with open(ruta, 'r', encoding= 'utf-8') as archivo:

            for linea in archivo:

                line = linea.strip().split()

                letra = line[0]
                col4 = line[4].split(',')
                if letra in letras:
                    contador = 0
                    for par in col4:
                        let, valor = par.split(":")
                        valor = int(valor)
                        contador += valor
                    
                    letras[letra] += contador
                else:
                    contador = 0
                    for par in col4:
                        let, valor = par.split(":")
                        valor = int(valor)
                        contador += valor

                    letras[letra] = contador


            resultado = {k: letras[k] for k in sorted(letras)}

            return resultado

print(pregunta_12())

    
