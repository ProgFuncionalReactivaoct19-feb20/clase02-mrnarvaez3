"""
	practica 1: Desarrollar la función anónima que retorne True or 
	False si el número dado es par.

	Ejemplo de llamada

	print(valor_par(2))
	print(valor_par(3))
	print(valor_par(11))
	Autor: Roberto N
"""
#  Funcion lambda para obtener true o false segun si es par o no
mifuncion = (lambda x: x%2==0)


print(mifuncion(2))
print(mifuncion(3))
print(mifuncion(11))
