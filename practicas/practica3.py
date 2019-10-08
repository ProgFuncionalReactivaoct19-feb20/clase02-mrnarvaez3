"""
	Practica 3:Dada la siguiente llamada a una función anónima:

	suma(10,11)

	Desarrollar la función; debe presentar en pantalla para el ejemplo 21
	autor: Roberto N
"""
suma = (10,11)
#  Funcion lambda para sumar cifras
mifuncion = lambda x: x[0] + x[1]

#  Salida de datos
print(mifuncion(suma))