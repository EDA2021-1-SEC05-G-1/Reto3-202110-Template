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
    print("5- Encontrar música para estudiar")
    print("6- Estimar las reproducciones de los géneros musicales")
    print("0-Salir")
    print("*******************************************")

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
        print("Se creo el catalogo sin información correctamente.")
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        answer=controller.loadData(cont, contexto,user)
        cont=answer[0]

        print("Hay "+str(lt.size(cont["tracks"]))+" tracks cargados.")
        print("Hay "+str(om.size(cont['artist_id']))+" artistas unicos cargados.")
        print("Hay "+str(om.size(cont['created_at']))+" eventos cargados.")
        print('Hay '+str(om.size(cont['instrumentalness']))+" HASHTAG")
    
        print("Tiempo [ms]: ", f"{answer[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[2]:.3f}")
    elif int(inputs[0]) ==3:
        caracteristica=str(input("Ingrese una caracteristica: "))
        minimo=float(input("Ingrese el valor minimo del contenido: "))
        maximo=float(input("Ingrese el valor maximo del contenido: "))
        respuesta=controller.req1(caracteristica,minimo,maximo,cont)
        tamano=respuesta[0][0]
        cantidad=respuesta[0][1]
        print("El total de artistas unicos son: "+str(tamano))
        print("El total de tracks o reproducciones son: "+str(cantidad))
        print("Tiempo [ms]: ", f"{respuesta[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{respuesta[2]:.3f}")
    elif int(inputs[0]) ==4:
        minimoE=float(input("Ingrese el valor minimo de la caracteristica Energy: "))
        maximoE=float(input("Ingrese el valor maximo de la caracteristica Energy: "))
        minimoD=float(input("Ingrese el valor minimo de la caracteristica Danceability: "))
        maximoD=float(input("Ingrese el valor maximo de la caracteristica Danceability: "))
        answers=controller.req2(cont,minimoE,maximoE,minimoD,maximoD)
        answersi=answers[0]
        cantidadii=lt.size(answersi)
        pista=lt.newList("ARRAY_LIST")
        print('Energy esta entre '+str(minimoE)+ " y "+str(maximoE))
        print("Danceability esta entre "+str(minimoD)+ " y "+str(maximoD))
        print("Los track unicos en eventos son: "+str(cantidadii))
        x=1
        while x<=5:
            rand=random.randint(1,cantidadii)# Aqui buscamos obtener un numero dentro del rango para poder usar el lt.getElement() de una pos cualquiera para imprimir
            track=lt.getElement(answersi,rand) #Lo mismo que it.next(de un iterador de lista)
            id=me.getValue(mp.get(track,'track_id')) #Saco pareja llave-valor del track_id y su valor (track_id respectivo del elemento), para luego sacar su valor(track_id)
            energia=me.getValue(mp.get(track,'energy'))
            danceability=me.getValue(mp.get(track,'danceability'))
            print("*******************************************")
            print('Track '+str(x)+':'+str(id)+ " with energy of "+str(energia)+" and danceability of "+str(danceability))
            x+=1
        print("Tiempo [ms]: ", f"{answers[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answers[2]:.3f}")
    elif int(inputs[0]) ==5:
        minimoI=float(input("Ingrese el valor minimo de la caracteristica instrumentalness: "))
        maximoI=float(input("Ingrese el valor maximo de la caracteristica instrumentalness: "))
        minimoT=float(input("Ingrese el valor minimo de la caracteristica tempo: "))
        maximoT=float(input("Ingrese el valor maximo de la caracteristica tempo: "))
        answersa=controller.req3(cont,minimoI,maximoI,minimoT,maximoT)
        asnwer=answersa[0]
        cantidad=lt.size(asnwer)
        pista=lt.newList("ARRAY_LIST")
        #pes=lt.getElement(answer,1) #Es lo mismo que it.next(f)
        print('Instrumentalness esta entre '+str(minimoI)+ " y "+str(maximoI))
        print("Tempo esta entre "+str(minimoT)+ " y "+str(maximoT))
        print("Los track unicos en eventos son: "+str(cantidad))
        x=1
        while x<=5:
            rand=random.randint(1,cantidad)
            track=lt.getElement(asnwer,rand) #Lo mismo que it.next(de un iterador de lista)
            id=me.getValue(mp.get(track,'track_id')) #Saco pareja llave-valor del track_id y su valor (track_id respectivo del elemento), para luego sacar su valor(track_id)
            instrumental=me.getValue(mp.get(track,'instrumentalness'))
            tempo=me.getValue(mp.get(track,'tempo'))
            print("*******************************************")
            print('Track '+str(x)+':'+str(id)+ " with instrumentalness of "+str(instrumental)+" and tempo of "+str(tempo))
            x+=1
        print("Tiempo [ms]: ", f"{answersa[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answersa[2]:.3f}")
    elif int(inputs[0]) ==6:
        generos=['POP','REGGAE','DOWN-TEMPO','CHILL-OUT','HIP-HOP','JAZZ AND FUNK','R&B','ROCK','METAL']
        x=input("Para buscar algun genero conocido (F) o desea crear un nuevo genero (V): ").upper()
        if x=="F":
            n=False
            lista=lt.newList()
            tamano=0
            print("*******************************************")
            print("Recuerde poner los generos que se desea buscar en mayuscula...")
            while n==False:
                print("*******************************************")
                print("Estos son los tipos de generos que puede buscar: ")
                print(generos)
                print("*******************************************")
                y=input("Ponga X para decir que genero desea buscar, de lo contrario marque E: ")
                if y=="X":
                    genero=input("Ingrese el genero que quiere buscar: ").upper()
                    if genero not in generos:
                        print("*******************************************")
                        print("Ingrese un genero valido que este dentro de la lista porfavor...")
                    else:
                        tamano+=1
                        lt.addLast(lista,genero)
                else: 
                    n=True
            q=0
            fua=it.newIterator(lista)
            while it.hasNext(fua):
                genero=it.next(fua)
                if genero=="POP":
                    minimo=100.0
                    maximo=130.0
                elif genero=='REGGAE':
                    minimo=60.0
                    maximo=90.0
                elif genero=='DOWN-TEMPO':###
                    minimo=70.0
                    maximo=100.0
                elif genero=='CHILL-OUT':#
                    minimo=90.0
                    maximo=120.0
                elif genero=='HIP-HOP':#
                    minimo=85.0
                    maximo=115.0
                elif genero=='JAZZ AND FUNK':
                    minimo=120.0
                    maximo=125.0
                elif genero=='R&B':
                    minimo=60.0
                    maximo=80.0
                elif genero=="ROCK":
                    minimo=110.0
                    maximo=140.0
                else:
                    minimo=100.0
                    maximo=160.0
                pra=controller.req4('tempo',minimo,maximo,cont)
                artistas=pra[0][0]
                reproducciones=pra[0][1]
                lista=pra[0][2]
                x=1
                cantidad=lt.size(lista)
                print("Para el genero: "+str(genero)+ ' se tiene que hay ' + str(artistas)+ ' artistas y '+ str(reproducciones)+' reproducciones')
                print("donde el tempo minimo es "+str(minimo)+ " y el maximo es "+ str(maximo))
                while x<=10:
                    rand=random.randint(1,cantidad) #
                    track=lt.getElement(lista,rand) #Lo mismo que it.next(de un iterador de lista)
                    id=me.getValue(mp.get(track,'track_id')) #Saco pareja llave-valor del track_id y su valor (track_id respectivo del elemento), para luego sacar su valor(track_id)
                    print("*******************************************")
                    print('Arist '+str(x)+':'+str(id))
                    x+=1
            print("Tiempo [ms]: ", f"{pra[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{pra[2]:.3f}")
        else:
            nombre=input("Ingrese el nuevo nombre del genero: ")
            minimo=float(input("Ingrese el valor minimo del tempo: "))
            maximo=float(input("Ingrese el valor maximo del tempo: "))
            pra=controller.req4('tempo',minimo,maximo,cont)
            artistas=pra[0][0]
            reproducciones=pra[0][1]
            lista=pra[0][2]
            x=1
            cantidad=lt.size(lista)
            print("*******************************************")
            print("Para el nuevo genero: "+str(nombre)+ ' se tiene que hay ' + str(artistas)+ ' artistas y '+ str(reproducciones)+' reproducciones')
            print("donde el tempo minimo es "+str(minimo)+ " y el maximo es "+ str(maximo))
            while x<=10:
                rand=random.randint(1,cantidad) #
                track=lt.getElement(lista,rand) #Lo mismo que it.next(de un iterador de lista)
                id=me.getValue(mp.get(track,'track_id'))
                print('Arist '+str(x)+':'+str(id))
                x+=1
            print("Tiempo [ms]: ", f"{pra[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{pra[2]:.3f}")
        pass
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
    