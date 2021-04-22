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
from DISClib.ADT import map as m
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
                'acousticness':None,
                'artist_id':None
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
            updatetrack(analyzer[caracteristica], track,caracteristica)
    return analyzer


def updatetrack(map, track,caracteristica):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    trackdate = track[caracteristica]
    entry = om.get(map, trackdate)
    if entry is None:
        datentry = newDataEntry(track,caracteristica)
        om.put(map, trackdate, datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, track,caracteristica)
    return map

def addDateIndex(datentry, track,caracteristica):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lst'+str(caracteristica)]
    lt.addLast(lst, track)
    trackindex = datentry[str(caracteristica)+"de"]
    offentry = m.get(trackindex, track[caracteristica]) #Poner lo que pide el usuario para el req1
    if (offentry is None):
        entry = newOffenseEntry(track[caracteristica], track,caracteristica)
        lt.addLast(entry[str(caracteristica)+"oe"], track)
        m.put(trackindex, track[caracteristica], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry[str(caracteristica)+"oe"], track)
    return datentry

def newOffenseEntry(offensegrp, crime,caracteristica):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {caracteristica: None, (str(caracteristica)+"oe"): None}
    ofentry[caracteristica] = offensegrp
    ofentry[(str(caracteristica)+"oe")] = lt.newList('SINGLELINKED', comparetrackindex)
    return ofentry

def newDataEntry(track,caracteristica):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {(str(caracteristica)+"de"): None, ('lst'+str(caracteristica)): None}
    entry[(str(caracteristica)+"de")] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=comparetrackindex)
    entry[('lst'+str(caracteristica))] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

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
