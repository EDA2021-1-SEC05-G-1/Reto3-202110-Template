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
    return analyzer
# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo
def req1(caracteristica,minimo,maximo,cont):
    return model.req1
def req2(cont,minimoE,maximoE,minimoD,maximoD):
    return model.req2(cont,minimoE,maximoE,minimoD,maximoD)