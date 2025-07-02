"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """ 

    ruta = "files/input/data.csv"
    meses = {}
    if os.path.exists(ruta):

        with open(ruta, 'r', encoding='utf-8') as archivo:

            for linea in archivo:
                line = linea.strip().split()

                fecha  = line[2].split('-')
                mes = fecha[1]
                if mes in meses:
                    meses[mes] += 1
                else:
                    meses[mes] = 1

            resultado = sorted([(mes, cantidad) for mes, cantidad in meses.items()])
            return resultado
    
    else:
        print("La ruta no existe")

    

print(pregunta_04())
   