"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
import datetime
import csv
import time
import tracemalloc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos
def loadData(analyzer, contexto,user):
    """
    Carga los datos de los archivos CSV en el modelo
    """

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    contexto = cf.data_dir + contexto
    input_file = csv.DictReader(open(contexto, encoding="utf-8"),delimiter=",")
    user= cf.data_dir + user
    input_file2 = csv.DictReader(open(user, encoding="utf-8"),delimiter=",")
    lst=[]
    for hashtag in input_file2:
        lst+=[hashtag["hashtag"]]
    i=0
    for track in input_file:
        track["hashtag"]=lst[i]
        model.addTrack(analyzer, track)
        i+=1
    
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return analyzer,delta_time, delta_memory
# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo
def req1(caracteristica,minimo,maximo,cont):

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    respuesta=model.req1(caracteristica,minimo,maximo,cont)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return respuesta,delta_time, delta_memory
def req2(cont,minimoE,maximoE,minimoD,maximoD):

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    respuesta=model.req2(cont,minimoE,maximoE,minimoD,maximoD)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return respuesta,delta_time, delta_memory
def req3(cont,minimoT,maximoT,minimoI,maximoI):

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    respuesta=model.req3(cont,minimoT,maximoT,minimoI,maximoI)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return respuesta,delta_time, delta_memory

# ======================================
# Funciones para medir tiempo y memoria
# ======================================


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)



def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
