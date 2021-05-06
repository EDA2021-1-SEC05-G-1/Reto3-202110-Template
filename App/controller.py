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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf
from DISClib.DataStructures import orderedmapstructure as mo
from DISClib.DataStructures import listiterator as it

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
def loadData(analyzer, contexto,user,sentiment):
    """
    Carga los datos de los archivos CSV en el modelo
    """

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    #sentimen = cf.data_dir + sentiment
    #input_file3 = csv.DictReader(open(sentimen, encoding="utf-8"),delimiter=",")
    contexto = cf.data_dir + contexto
    input_file = csv.DictReader(open(contexto, encoding="utf-8"),delimiter=",")
    #user= cf.data_dir + user
    #input_file2 = csv.DictReader(open(user, encoding="utf-8"),delimiter=",")
    #x=0
    #lst=lt.newList()
    #sss=lt.newList()
   # for senti in input_file3:
    #    lt.addLast(sss,senti)
    #itet=it.newIterator(sss)
    #x=0
    #lst=lt.newList()
    #for hashtag in input_file2:
    #    lt.addLast(lst,hashtag)
    #new=it.newIterator(lst)
        #x+=1
        #if x==5: 
            #break#Se usaba para mirar que cantidad de datos mirar
    #i=0"instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness",
    # "energy","mode","key","artist_id","tweet_lang","track_id","created_at","lang","time_zone","user_id","id"
    x=0 
    for track in input_file:
        #No es lo mismo comparar str que con numeros
        track['tempo']=float(track['tempo'])#Se habia hecho primero un orden de str(eterolexico?(que se comparan str en om.values())) Es necesario tenerlos en int
        track['energy']=float(track['energy'])
        track['liveness']=float(track['liveness'])
        track['instrumentalness']=float(track['instrumentalness'])
        hora=track['created_at'][11:19]
        t=datetime.time.fromisoformat(hora)#Fromisoformat crea un formato iso del datetime() Formato de libreria para poder hacer operaciones (su inversa es isoFormat (ponerlo en str))
        track['horas']=t
        track['created_at']=str(track['created_at'])
        track['speechiness']=float(track['speechiness'])
        track['danceability']=float(track['danceability'])
        track['valence']=float(track['valence'])
        track['user_id']=int(track['user_id'])
        track['loudness']=float(track['loudness'])
        track['acousticness']=float(track['acousticness'])
        track['energy']=float(track['energy'])
        track['mode']=float(track['mode'])
        track['key']=float(track['key'])
        track['id']=int(track['id'])
        #track['hashtag']=""
        #track['hashtag']=lt.getElement(lst,x+1)
        #if track['hashtag']==None:
            #track['hashtag']=""
        #for x in 
        model.addTrack(analyzer, track)
        x+=1
        if x==1000: #Se usaba para mirar que cantidad de datos mirar
            break
        #i+=1
    
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

def req4(caracteristica,minimo,maximo,cont):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    respuesta=model.req4(caracteristica,minimo,maximo,cont)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return respuesta,delta_time, delta_memory
# =======================Req 5===========
def total(cont,miniH,miniM,miniS,maxH,maxM,maxS):
    return model.total(cont,miniH,miniM,miniS,maxH,maxM,maxS)
def init2():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer2()
    return analyzer
def loadData2(analyzer, contexto,user,sentiment):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    sentimen = cf.data_dir + sentiment
    input_file3 = csv.DictReader(open(sentimen, encoding="utf-8"),delimiter=",")
    contexto = cf.data_dir + contexto
    #input_file = csv.DictReader(open(contexto, encoding="utf-8"),delimiter=",")
    #user= cf.data_dir + user
    input_file2 = csv.DictReader(open(user, encoding="utf-8"),delimiter=",")
    #x=0
    lst=lt.newList()
    sss=lt.newList()
    for senti in input_file3:
        lt.addLast(sss,senti)
    itet=it.newIterator(sss)
    #x=0
    for hashtag in input_file2:
        lt.addLast(lst,hashtag['hashtag'])
     #   x+=1
      #  if x==5: 
       #     break#Se usaba para mirar que cantidad de datos mirar
    #i=0"instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness",
    # "energy","mode","key","artist_id","tweet_lang","track_id","created_at","lang","time_zone","user_id","id"
    x=0 
    for track in input_file:
        #No es lo mismo comparar str que con numeros
        track['tempo']=float(track['tempo'])#Se habia hecho primero un orden de str(eterolexico?(que se comparan str en om.values())) Es necesario tenerlos en int
        hora=track['created_at'][11:19]
        t=datetime.time.fromisoformat(hora)#Fromisoformat crea un formato iso del datetime() Formato de libreria para poder hacer operaciones (su inversa es isoFormat (ponerlo en str))
        track['horas']=t
        track['created_at']=str(track['created_at'])
        track['user_id']=int(track['user_id'])
        track['id']=int(track['id'])
        while it.hasNext(itet):
            sent=it.next(itet)
            if sent['hashtag']==lt.getElement(lst,x+1):
                track['vader_avg']=sent['vader_avg']
                track["hashtag"]=lt.getElement(lst,x+1)
                model.addTrack(analyzer,track)
                break
        itet=it.newIterator(sss)
        #for x in 
        #model.addTrack(analyzer, track)
        x+=1
        if x==100: #Se usaba para mirar que cantidad de datos mirar
            break
        #i+=1
    return analyzer
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
