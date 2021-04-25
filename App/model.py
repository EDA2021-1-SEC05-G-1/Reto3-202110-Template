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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import datetime
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los tracks
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """"instrumentalness","liveness","speechiness","danceability","valence"
    analyzer = {'tracks': None,
                'instrumentalness':None,
                'speechiness':None,
                'liveness':None,
                'energy':None,
                'danceability':None,
                'valence':None,
                'tempo':None,
                'acousticness':None,
                'artist_id':None
                #'hashtag':None
                }
    analyzer['tracks'] = lt.newList('SINGLE_LINKED', compareIds)
    for parte in analyzer:
        if parte!='tracks':
            analyzer[parte]=om.newMap(omaptype='RBT',
                                      comparefunction=compareTracks)
    return analyzer

# Funciones para agregar informacion al catalogo

def addTrack(analyzer, track):
    """
    """
    lt.addLast(analyzer['tracks'], track)
    for caracteristica in analyzer:
        if caracteristica!='tracks':
            updatetrack(analyzer[caracteristica], track,caracteristica,analyzer)
    return analyzer

def updatetrack(map,track,caracteristica,catalogo):
    data = track[caracteristica]
    entry = om.get(map, data)
    if entry is None:
        lst=lt.newList('ARRAY_LIST')
    else:
        lst = me.getValue(entry)
    informacion_track=newDataEntry(catalogo,track)
    lt.addLast(lst,informacion_track)
    om.put(map, data, lst)
    return map
def newDataEntry(catalogo,track):
    entrada = mp.newMap(numelements=10,maptype='PROBING',loadfactor=0.5)
    for caracteristica in catalogo:
        if caracteristica!='tracks':
            mp.put(entrada,caracteristica,track[caracteristica])
    mp.put(entrada,'track_id',track['track_id'])
    mp.put(entrada,'user_id',track['user_id'])
    return entrada

# Funciones para creacion de datos

# Funciones de consulta
def req1(caracteristica,minimo,maximo,cont):

    lst=om.keys(cont[caracteristica],minimo,maximo)
    size=lt.size(lst)
    return size
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareTracks(track1, track2):
    """
    Compara dos tracks
    """
    if (track1 == track2):
        return 0
    elif (track1 > track2):
        return 1
    else:
        return -1
def comparetrackindex(track1, track2):
    """
    Compara dos tipos de crimenes
    """
    offense = me.getKey(track2)
    if (track1 == offense):
        return 0
    elif (track1 > offense):
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1