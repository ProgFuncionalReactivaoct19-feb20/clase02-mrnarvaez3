"""
	practica 2: Desarrollar una función anónima que permita retornar la siguiente salida, ejemplo:

	CUENCA capital de AZUAY

	La llamada a la función es

	print(cadena_personalizada("Cuenca", "Azuay"))
	Autor: Roberto N
"""
#  Funcion Lambda para concatenar cadenas 

cadena_personalizada = lambda x, y: "%s capital de %s" %(x.upper(), y.upper())

#  Saliuda de datos
print(cadena_personalizada("Cuenca", "Azuay"))