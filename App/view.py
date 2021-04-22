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
assert cf


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
    print("0-Salir")
    print("*******************************************")

catalog = None
contexto= "context_content_features-small.csv"
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
        controller.loadData(cont, contexto)

        print("Hay "+str(lt.size(cont["tracks"]))+" tracks cargados.")
       
    elif int(inputs[0]) ==3:
        caracteristica=str(input("Ingrese una caracteristica: "))
        minimo=input("Ingrese el valor minimo del contenido: ")
        maximo=input("Ingrese el valor minimo del contenido: ")
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
        
    else:
        sys.exit(0)
sys.exit(0)
