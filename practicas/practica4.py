"""
	Practica 4:Dada la siguiente estructura de datos

	[10,2,8,7,5,4,3,11,0, 1]

	Use:
	Función map
	Una función anónima
	que permita presentar en otra lista, cada elemento elevado a la tercera potencia.
	Autor: Roberto N
"""
lista = [10,2,8,7,5,4,3,11,0,1]
#  Funcion lambda para elevar numero al cubo
mifuncion = lambda x: x**3


#  salida de datos
print(list(map(mifuncion, lista)))