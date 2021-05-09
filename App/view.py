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
import datetime
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
from App import model
import csv

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
    print("7- Indicar el género musical más escuchado en un tiempo")
    print("0-Salir")
    print("*******************************************")

contexto= "context_content_features-small.csv"
user="user_track_hashtag_timestamp-small.csv"
sentiment="sentiment_values.csv"
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
        answer=controller.loadData(cont, contexto,user,sentiment)
        cont=answer[0] #Se saca el catalogo de la tupla de respuesta
        answer2=controller.loadata1(sentiment)
        sss=answer2[0]
        answer3=controller.loadata2(user)
        lsta=answer3[0]
        memoria=answer[2]+answer2[2]+answer3[2]
        tiempo=answer[1]+answer2[1]+answer3[1]
        print("Hay "+str(lt.size(cont["tracks"]))+" tracks cargados.")
        print("Hay "+str(om.size(cont['artist_id']))+" artistas unicos cargados.")
        print("Hay "+str(om.size(cont['created_at']))+" eventos cargados.")
        print("Tiempo [ms]: ", f"{tiempo:.3f}", "  ||  ", #Imprime el tiempo
              "Memoria [kB]: ", f"{memoria:.3f}") #Imprime la memoria
    elif int(inputs[0]) ==3:
        caracteristica=str(input("Ingrese una caracteristica: "))
        minimo=float(input("Ingrese el valor minimo del contenido: "))
        maximo=float(input("Ingrese el valor maximo del contenido: "))
        respuesta=controller.req1(caracteristica,minimo,maximo,cont)
        tamano=respuesta[0][0] #Se saca el total de los artistas unicos desde el req1 (sale de tupla de la respuesta)
        cantidad=respuesta[0][1] #Se saca el total de tracks no unicos (sale de tupla de la respuesta)
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
        answersi=answers[0] #Sale la lista de respuesta 
        cantidadii=lt.size(answersi) #Se saca el tamaño de la lista de la respuesta
        pista=lt.newList("ARRAY_LIST")#Crea una nueva lista para iterar, con el fin de imprimir 5 tracks random
        print('Energy esta entre '+str(minimoE)+ " y "+str(maximoE))
        print("Danceability esta entre "+str(minimoD)+ " y "+str(maximoD))
        print("Los track unicos en eventos son: "+str(cantidadii))
        x=1
        while x<=5:
            rand=random.randint(1,cantidadii)# Aqui buscamos obtener un numero dentro del rango para poder usar el lt.getElement() de una pos cualquiera para imprimir
            track=lt.getElement(answersi,rand) #Lo mismo que it.next(de un iterador de lista) #Sacamos un pedazo de la lista random
            id=me.getValue(mp.get(track,'track_id')) #Saco pareja llave-valor del track_id y su valor (track_id respectivo del elemento), para luego sacar su valor(track_id)
            energia=me.getValue(mp.get(track,'energy'))#Saco el valor de la pareja llave-valor del energy 
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
                y=input("Ponga X para decir que genero desea buscar, de lo contrario marque E: ").upper()
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
            sumat=0
            sumam=0
            total=0
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
                total+=int(reproducciones)
                sumat+=float(pra[1])
                sumam+=float(pra[2])
                print("*******************************************")
                print("*******************************************")
                print("Para el genero: "+str(genero)+ ' se tiene que hay ' + str(artistas)+ ' artistas y '+ str(reproducciones)+' reproducciones')
                print("Donde el tempo minimo es "+str(minimo)+ " y el maximo es "+ str(maximo))
                while x<=10:
                    rand=random.randint(1,cantidad) #
                    track=lt.getElement(lista,rand) #Lo mismo que it.next(de un iterador de lista)
                    id=me.getValue(mp.get(track,'track_id')) #Saco pareja llave-valor del track_id y su valor (track_id respectivo del elemento), para luego sacar su valor(track_id)
                    print("*******************************************")
                    print('Arist '+str(x)+':'+str(id))
                    x+=1
            print("En total se tiene un total de reproducciones de:  "+str(total))
            print("Tiempo [ms]: ", f"{sumat:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{sumam:.3f}")
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
            print("*******************************************")
            print("Para el nuevo genero: "+str(nombre)+ ' se tiene que hay ' + str(artistas)+ ' artistas y '+ str(reproducciones)+' reproducciones')
            print("Donde el tempo minimo es "+str(minimo)+ " y el maximo es "+ str(maximo))
            while x<=10:
                rand=random.randint(1,cantidad) #
                track=lt.getElement(lista,rand) #Lo mismo que it.next(de un iterador de lista)
                id=me.getValue(mp.get(track,'track_id'))
                print('Arist '+str(x)+':'+str(id))
                x+=1
            print("Tiempo [ms]: ", f"{pra[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{pra[2]:.3f}")
    elif int(inputs[0]) ==7:
        print('Ingrese los datos de las horas en formato de 1-24 horas dependiendo del rango que desea')
        miniH=int(input("Ingrese el(las) hora(s) minima(s) a trabajar: "))
        miniM=int(input("Ingrese el(los) minuto(s) minimo(s) a trabajar: "))
        miniS=int(input("Ingrese el(los) segundo(s) minimo(s) a trabajar: "))
        maxH=int(input("Ingrese el(las) hora(s) maxima(s) a trabajar: "))
        maxM=int(input("Ingrese el(los) minuto(s) maximo(s) a trabajar: "))
        maxS=int(input("Ingrese el(los) segundo(s) maximo(s) a trabajar: "))
        resp1=controller.total(cont,miniH,miniM,miniS,maxH,maxM,maxS)
        filtrada1=resp1[0]
        memoria_t=resp1[2]
        tiempo_t=resp1[1]
        nuevo_cat=controller.init2()
        resp2=controller.catalogo2(lsta,sss,filtrada1,nuevo_cat)
        nuevo_cat=resp2[0]
        memoria_t+=resp2[2]
        tiempo_t+=resp2[1]
        generos=lt.newList()
        lista=['POP','REGGAE','DOWN-TEMPO','CHILL-OUT','HIP-HOP','JAZZ AND FUNK','R&B','ROCK','METAL']#VIEW
        for gen in lista:
            lt.addLast(generos,gen)
        fua=it.newIterator(generos)
        top=0
        nombretop=""
        listatop=None
        cantidadT=0
        sumat=0
        sumam=0
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
            pra=controller.req4('tempo',minimo,maximo,nuevo_cat)
            artistas=pra[0][0]
            reproducciones=pra[0][1]
            lista=pra[0][2]
            sumat+=float(pra[1])
            sumam+=float(pra[2])
            cantidadT+=reproducciones
            if top<reproducciones:
                top=reproducciones
                nombretop=genero
                listatop=lista
            x=1
            cantidad=lt.size(lista)
            print("*******************************************")
            print("*******************************************")
            print("Para el genero: "+str(genero)+ ' se tiene que hay ' + str(artistas)+ ' artistas y '+ str(reproducciones)+' reproducciones')
            print("Donde el tempo minimo es "+str(minimo)+ " y el maximo es "+ str(maximo))
        print("En total se tienen "+ str(cantidadT) + " reproducciones o tracks en la hora "+ str(miniH)+":"+str(miniM)+":"+str(miniS)+" y la hora "+str(maxH)+":"+str(maxM)+":"+str(maxS))
        tiempo_t+=sumat
        memoria_t+=sumam
        print("=====================================")
        print("*************************************")
        resp3=controller.top(listatop)
        topsin=resp3[0]
        tiempo_t+=resp3[1]
        memoria_t+=resp3[2]
        lst=topsin[0]
        paaa=topsin[1]
        totalu=lt.size(lst)
        print("El genero con mayor reproducciones (TOP) es: "+str(nombretop) +" con "+str(totalu)+" de tracks unicos")
        x=1
        print("*******************************************")
        print("*******************************************")
        print("Estos son algunos de los tracks del genero: ")
        vistos=lt.newList()
        n=1
        while n<=10:
            rand=random.randint(1,totalu) 
            track=lt.getElement(paaa,rand) 
            id=me.getValue(mp.get(track,'track_id'))
            hashte=me.getValue(mp.get(track,'cantidad'))
            vader=me.getValue(mp.get(track,'vader_avg'))
            if lt.isPresent(vistos,id)==0:
                print('Track '+str(x)+':'+str(id) +" con "+str(hashte)+" hashtags y con un vader avg de "+str(vader))
                lt.addLast(vistos,id)
                x+=1
            n+=1
        print("Tiempo [ms]: ", f"{tiempo_t:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{memoria_t:.3f}") 
    else:
        sys.exit(0)
sys.exit(0)

    