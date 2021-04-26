"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import orderedmapstructure as mo
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
assert cf
import random


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar el catálogo")
    print("2- Cargar información en el catalogo")
    print("3- Caracterizar las reproducciones")
    print("4- Encontrar música para festejar")
    print("0-Salir")
    print("*******************************************")

catalog = None
contexto= "context_content_features-small.csv"
user="user_track_hashtag_timestamp-small.csv"
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont, contexto,user)

        print("Hay "+str(lt.size(cont["tracks"]))+" tracks cargados.")
    elif int(inputs[0]) ==3:
        caracteristica=str(input("Ingrese una caracteristica: "))
        minimo=input("Ingrese el valor minimo del contenido: ")
        maximo=input("Ingrese el valor maximo del contenido: ")
        x=om.values(cont[caracteristica],minimo,maximo)
        i=0
        new=it.newIterator(x)
        cantidad=0
        cantidad2=0
        lst=lt.newList("SINGLE_LINKED")
        paaa=lt.newList("SINGLE_LINKED")
        while it.hasNext(new):
            l=it.next(new)
            cantidad2+=lt.size(l) #Reproducciones
            nuevo=it.newIterator(l)
            p=0
            while it.hasNext(nuevo):
                pedazo=it.next(nuevo)
                ax=mp.get(pedazo,'artist_id')
                tax=me.getValue(ax)
                if lt.isPresent(paaa,tax)==0:
                    lt.addLast(paaa,tax)
        print(lt.size(paaa)) #Cantidad de artistas unicos
        print(cantidad2) #Reproducciones se pasa por 12
    elif int(inputs[0]) ==4:
        minimoE=input("Ingrese el valor minimo de la caracteristica Energy: ")
        maximoE=input("Ingrese el valor maximo de la caracteristica Energy: ")
        minimoD=input("Ingrese el valor minimo de la caracteristica Danceability: ")
        maximoD=input("Ingrese el valor maximo de la caracteristica Danceability: ")
        answer=controller.req2(cont,minimoE,maximoE,minimoD,maximoD)
        cantidad=lt.size(answer)
        pista=lt.newList("ARRAY_LIST")
        peq1=random.randint(1,cantidad)
        #pes=lt.getElement(answer,1) #Es lo mismo que it.next(f)
        print('Energy esta entre '+str(minimoE)+ " y "+str(maximoE))
        print("Danceability esta entre "+str(minimoD)+ " y "+str(maximoD))
        print("Los track unicos en eventos son: "+str(cantidad))
        x=1
        while x<=5:
            rand=random.randint(1,cantidad)
            track=lt.getElement(answer,rand) #Lo mismo que it.next(de un iterador de lista)
            id=me.getValue(mp.get(track,'track_id')) #Saco pareja llave-valor del track_id y su valor (track_id respectivo del elemento), para luego sacar su valor(track_id)
            energia=me.getValue(mp.get(track,'energy'))
            danceability=me.getValue(mp.get(track,'danceability'))
            print("*******************************************")
            print('Track '+str(x)+':'+str(id)+ " with energy of "+str(energia)+" and danceability of "+str(danceability))
            x+=1
        #pista=lt.subList(answer,1,1)
        #x=1
        #f=it.newIterator(pista)
        #while it.hasNext(f):
 #           track=it.next(f)#Saca el mapa de 1 elemento #Lo mismo que lt.getElement()
  #          print(track)
   #         id=me.getValue(mp.get(track,'track_id')) #Saco pareja llave-valor del track_id y su valor (track_id respectivo del elemento), para luego sacar su valor(track_id)
    #        energia=me.getValue(mp.get(track,'energy'))
     #       danceability=me.getValue(mp.get(track,'danceability'))
      #      print("*******************************************")
       #     print('Track '+str(x)+':'+str(id)+ " with energy of "+str(energia)+" and danceability of "+str(danceability))
        #    x+=1
            #Literalmente van a imprimir los primeros 5 elementos de la lista que cumple con los criterios dados por el usuario
            #Por el orden en que se guardaron los datos (1 se guardaron los de energy y luego los de danceability que cumplian con los criterios)
        #0(n^2 + n^2)
        #return lt.size(lst),pista

    else:
        sys.exit(0)
sys.exit(0)

       # for f in range(0,lt.size(x)):#+1
        #    a=lt.getElement(x,f)
         #   cantidad+=lt.size(a)
          #  for n in range(0,lt.size(a)+1):#+1 para que se recorra todo
           #     f=lt.getElement(a,n)
            #    n=mp.get(f,'user_id')
             #   t=me.getValue(n)
              #  if lt.isPresent(lst,t)==0:
               #     lt.addLast(lst,t)
       # print(lt.size(lst))
        #print(cantidad)
        #Hacer conteo y un cmpfunction con el tadlist
       # tad=lt.newList('ARRAY_LIST')
        #lista_n=[]
        #i=1
        #while i<lt.size(x):
         #   if lt.getElement(x,i)
        #tad=lt.newList()
        #cont=mp.get()
       # nueva=lt.newList() #Nueva lista para empezar a meter para no repetir artistas
      #  validacion=om.values(cont[caracteristica],minimo,maximo)#Hacer un filtrado de la caracteristica desde lo que quiere el usuario
       # for x in range(1+lt.size(validacion)):
        #    parte=lt.getElement(validacion,x)
         #   peque=me.getValue(cont['user_id'])
          #  artista=mp.get(peque,'user_id')
           # if lt.isPresent(nueva,artista)==0:
            #    lt.addLast(artista)
      #  print(lt.size(validacion))
       # print(lt.size(nueva))
       #Para este requerimiento la idea era que a partir del mapa de los artistas de las llaves,
       #Contar cuantas veces tiene la caracteristica deseada en sus tracks y meterse a sus valores
       #Mirando que cumpla cada track con la caracteristica para poder sacar ese track en otro ordered map
       #Basicamente crear otro om para poder luego hacer .keys() y lt.size()
        #Otra solución propuesta fue que a partir del catalogo, crear un nuevo pedazo para el requerimiento en el mismo
        #Con el fin de que a partir de un catalogo base mirar que no se repitan losa artistas para ir guardando los datos,
        #Sin embargo, no entendimos ni logramos correctamente como sacar los datos del catalogo
        #Ahora bien, logramos llegar a tener un catalogo en base a las caracteristicas del contexto en el que se carga correctamente cada dato
  #  variable=input('Va a ingresar un genero musical unico?: ')
  #  diccionario={'regge':(60,90}....}
  #  if varibale=="Si":
  #      min=input("minimo: ")
   #     max=input("maximo: ")
     #   nombre=input("Nombre: ")
    #    x=om.values(cont['tempo'],min,max)
      #  diccionario[nombre]=x
    