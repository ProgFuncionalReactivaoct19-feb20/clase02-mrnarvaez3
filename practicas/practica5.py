"""
	Practica 5: Dada la siguiente estructura de datos

	[(10,2), (8,7), (5,4), (3,11), (10,11)]

	Use:
	Función map
	Dos funciones anónimas
	que permita presentar en otra lista; para las primeras posiciones la raiz cuadrada, 
	para las segundas posiciones el cuadrado del número
	Autor: Roberto N
"""
import math


datos = [(10,2), (8,7), (5,4), (3,11), (10,11)]
#  Lista de funciones lambda para obtener resultados
funcion1 = lambda x: x[0]
funcion2 = lambda x: x[1]
funcion3 = lambda x: (math.sqrt(funcion1(x)),funcion2(x)**2)
 
#  Salida de datos
print(list(map(funcion3 ,datos)))