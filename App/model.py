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
from DISClib.DataStructures import orderedmapstructure as mo
from DISClib.DataStructures import listiterator as it
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
                'artist_id':None,
                'created_at':None,
                'horas':None
                #'hashtag':None
                #'cantidad_hashtag':None
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
    informacion_track=newDataEntry(catalogo,track,caracteristica)
    lt.addLast(lst,informacion_track)
    om.put(map, data, lst)
    return map
def newDataEntry(catalogo,track,caracteristica):
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
    x=om.values(cont[caracteristica],minimo,maximo)
    i=0
    new=it.newIterator(x)
    cantidad=0
    cantidad2=0
    lst=lt.newList("SINGLE_LINKED")
    paaa=lt.newList("SINGLE_LINKED")
    while it.hasNext(new):
        l=it.next(new)
        cantidad2+=lt.size(l)
        #print(cantidad2) #Reproducciones
        nuevo=it.newIterator(l)
        while it.hasNext(nuevo):
            pedazo=it.next(nuevo)
            ax=mp.get(pedazo,'artist_id')
            tax=me.getValue(ax)
            if lt.isPresent(paaa,tax)==0:
                lt.addLast(paaa,tax)
    #print(lt.size(paaa)) #Cantidad de artistas unicos
    #print(cantidad2)
    tamano=lt.size(paaa)
    respuesta=(tamano,cantidad2)
    return respuesta
def req2(cont,minimoE,maximoE,minimoD,maximoD): #Cont es el catalogo
    energy=om.values(cont['energy'],minimoE,maximoE)
    dance=om.values(cont['danceability'],minimoD,maximoD)
    new=it.newIterator(energy)
    lst=lt.newList("SINGLE_LINKED")
    paaa=lt.newList("SINGLE_LINKED")
    while it.hasNext(new):
        l=it.next(new)
        nuevo=it.newIterator(l)
        while it.hasNext(nuevo):
            pedazo=it.next(nuevo) #Esto devuelve un mapa de la lista iterando (mapa de la lista(cada elemento))
            ax=mp.get(pedazo,'danceability')
            nex=mp.get(pedazo,'track_id')#Devuelve la llave danceability y el valor respectivo del mapa en forma de diccionario
            tax=me.getValue(ax)#Devuelve el valor de danceability del track sacado en el mapa de it.next(video)
            fex=me.getValue(nex)
            if float(tax)>=float(minimoD) and float(tax)<=float(maximoD):
                if lt.isPresent(lst,fex)==0:
                    lt.addLast(paaa,pedazo)
                    lt.addLast(lst,fex)
    new=it.newIterator(dance)
    while it.hasNext(new):
        l=it.next(new)
        nuevo=it.newIterator(l)
        while it.hasNext(nuevo):
            pedazo=it.next(nuevo) #Esto devuelve un mapa de la lista iterando (mapa de la lista(cada elemento))
            ax=mp.get(pedazo,'energy') #Devuelve la llave energy y el valor respectivo del mapa en forma de diccionario
            tax=me.getValue(ax)#Devuelve el valor de energy del track sacado en el mapa de it.next(video)
            yex=mp.get(pedazo,'track_id')
            tex=me.getValue(yex)
            if float(tax)>=float(minimoE) and float(tax)<=float(maximoE):
                if lt.isPresent(lst,tex)==0:
                    lt.addLast(paaa,pedazo)
                    lt.addLast(lst,tex)
    return paaa
def req3(cont,minimoI,maximoI,minimoT,maximoT): #Cont es el catalogo
    tempo=om.values(cont['tempo'],minimoT,maximoT)
    instr=om.values(cont['instrumentalness'],minimoI,maximoI)
    new=it.newIterator(tempo)
    lst=lt.newList("SINGLE_LINKED")
    paaa=lt.newList("SINGLE_LINKED")
    while it.hasNext(new):
        l=it.next(new)
        nuevo=it.newIterator(l)
        while it.hasNext(nuevo):
            pedazo=it.next(nuevo) #Esto devuelve un mapa de la lista iterando (mapa de la lista(cada elemento))
            ax=mp.get(pedazo,'instrumentalness')
            nex=mp.get(pedazo,'track_id')#Devuelve la llave danceability y el valor respectivo del mapa en forma de diccionario
            tax=me.getValue(ax)#Devuelve el valor de danceability del track sacado en el mapa de it.next(video)
            fex=me.getValue(nex)
            if float(tax)>=float(minimoI) and float(tax)<=float(maximoI):
                if lt.isPresent(lst,fex)==0:
                    lt.addLast(paaa,pedazo)
                    lt.addLast(lst,fex)
    new=it.newIterator(instr)
    while it.hasNext(new):
        l=it.next(new)
        nuevo=it.newIterator(l)
        while it.hasNext(nuevo):
            pedazo=it.next(nuevo) #Esto devuelve un mapa de la lista iterando (mapa de la lista(cada elemento))
            ax=mp.get(pedazo,'tempo') #Devuelve la llave energy y el valor respectivo del mapa en forma de diccionario
            tax=me.getValue(ax)#Devuelve el valor de energy del track sacado en el mapa de it.next(video)
            yex=mp.get(pedazo,'track_id')
            tex=me.getValue(yex)
            if float(tax)>=float(minimoT) and float(tax)<=float(maximoT):
                if lt.isPresent(lst,tex)==0:
                    lt.addLast(paaa,pedazo)
                    lt.addLast(lst,tex)
    return paaa
def req4(caracteristica,minimo,maximo,cont):
    x=om.values(cont[caracteristica],minimo,maximo)
    new=it.newIterator(x)
    cantidad=0
    cantidad2=0
    lst=lt.newList("SINGLE_LINKED")
    paaa=lt.newList("SINGLE_LINKED")
    while it.hasNext(new):
        l=it.next(new)
        cantidad2+=lt.size(l)
        nuevo=it.newIterator(l)
        while it.hasNext(nuevo):
            pedazo=it.next(nuevo)
            ax=mp.get(pedazo,'artist_id')
            tax=me.getValue(ax)
            if lt.isPresent(paaa,tax)==0: #No esta presente si es 0 #Miramos si el artist_id esta ahí
                lt.addLast(paaa,tax)
                lt.addLast(lst,pedazo)
    #print(lt.size(paaa)) #Cantidad de artistas unicos
    #print(cantidad2)
    tamano=lt.size(paaa)
    respuesta=(tamano,cantidad2,lst)
    return respuesta
# ==============req 5 =========
def total(cont,miniH,miniM,miniS,maxH,maxM,maxS):
    mini=datetime.time(miniH,miniM,miniS)
    maxi=datetime.time(maxH,maxM,maxS)
    filtrada=om.values(cont['horas'],mini,maxi)
    return filtrada
def newAnalyzer2():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los tracks
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """"instrumentalness","liveness","speechiness","danceability","valence"
    analyzer = {'tracks': None,
                'tempo':None,
                'artist_id':None,
                'track_id':None,
                'cantidad':None,
                'vader_avg':None #Para poder usarlos, necesitamos tenerlos como arboles para que se identifiquen (aparezcan en los tracks)
                }
    analyzer['tracks'] = lt.newList('SINGLE_LINKED', compareIds)
    for parte in analyzer:
        if parte!='tracks':
            analyzer[parte]=om.newMap(omaptype='RBT',
                                      comparefunction=compareTracks)
    return analyzer
def catalogo2(lsta,sss,filtrada1,nuevo_cat):#lsta es la lista de usuario_hashtag, sss la lista de todos los sentiment, newsaw es la lista del om.values en modo de iterar
    newsaw=it.newIterator(filtrada1)
    new=it.newIterator(lsta)# Ponerlo en controller
    itet=it.newIterator(sss)# Ponerlo en otro controllorer junto 
    while it.hasNext(newsaw):#Model, SE NECESITA EL CATALOGO NUEVO--PASARLO COMO PARAMETRO 
            l=it.next(newsaw)#DESDE AQUI HASTA DONDE TE MARQUE ABAJO CON &&&&&&&&&&&&&&&&&&&&& VA EN MODEL
            #cantidad2+=lt.size(l)
            #print(cantidad2) #Reproducciones
            nuevo=it.newIterator(l)
            while it.hasNext(nuevo):
                pedazo=it.next(nuevo) #Mira cada track cumplido con el primer filtro
                #ax=mp.get(pedazo,'hashtag')
                ex=mp.get(pedazo,'tempo')
                ix=mp.get(pedazo,'horas')
                ox=mp.get(pedazo,'track_id')
                ux=mp.get(pedazo,'user_id')
                ax=mp.get(pedazo,'artist_id')
                #tax=me.getValue(ax)
                tex=me.getValue(ex)
                tix=me.getValue(ix)
                tox=me.getValue(ox)
                tux=me.getValue(ux)
                tax=me.getValue(ax)
                cantidad=0
                vader_avg=0
                while it.hasNext(new):
                    hashtag=it.next(new) #Buscar el hashtag aqui y su valor vader tambien #Mira cada hashtag 
                    if hashtag['track_id']==tox:
                        hasht=hashtag['hashtag'].lower() #Se busca los que sean iguales al track_id (todos los hashtag del track_id respectivo)
                        while it.hasNext(itet):
                            senti=it.next(itet) #Se busca basicamente que tenga un valor_vader
                            if senti['hashtag'].lower()==hasht:
                                if senti['vader_avg']=='' or senti['vader_avg']==None:
                                    vader_avg+=0
                                    cantidad+=1
                                else:
                                    cantidad+=1
                                    vader_avg+=float(senti['vader_avg'])
                                #if senti['vader_avg']!='' and senti['vader_avg']!=None:
                                 #   vader_avg+=float(senti['vader_avg'])
                                  #  cantidad+=1
                                break
                        itet=it.newIterator(sss)
                new=it.newIterator(lsta)
                nuevodic={}
                nuevodic['tempo']=float(tex)
                nuevodic['horas']=tix
                nuevodic['track_id']=tox
                nuevodic['artist_id']=tax
                nuevodic['cantidad']=cantidad
                nuevodic['user_id']=tux
                if nuevodic['cantidad']!=0: 
                    vader_avg=vader_avg/cantidad
                    nuevodic['vader_avg']=vader_avg
                    addTrack(nuevo_cat,nuevodic) 
    return nuevo_cat
def top(listatop):
    newisi=it.newIterator(listatop)#NECESITAS CREAR ESTA VARIABLE EN MODEL, PERO PARA ELLO NECESITAS CREAR UNA NUEVA FUNCION QUE TE LLEVE TODO LO DEL TOP HACIA MODEL Y HACER LO DE ABAJO
    lst=lt.newList("SINGLE_LINKED")#MODEL
    paaa=lt.newList("SINGLE_LINKED")#MODEL
    while it.hasNext(newisi):#DESDE AQUI HASTA QUE SE VUELVAS A VER @@@@@@@@@@@@@@@@@@@@@@@ VA EN MODEL
        pedazo=it.next(newisi)#Esto devuelve un mapa de la lista iterando (mapa de la lista(cada elemento))
        nex=mp.get(pedazo,'track_id')#Devuelve la llave danceability y el valor respectivo del mapa en forma de diccionario
            #tax=me.getValue(ax)#Devuelve el valor de danceability del track sacado en el mapa de it.next(video)
        fex=me.getValue(nex)
        if lt.isPresent(lst,fex)==0:
            lt.addLast(paaa,pedazo)
            lt.addLast(lst,fex)
    return lst,paaa
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