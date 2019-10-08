"""
	Ejemplo 1: uso de funcion lambda
"""

lista = [10,2,3,5]
# print(min(lista, key=lambda x: x))
print(min(lista, key=lambda x: x+100))
