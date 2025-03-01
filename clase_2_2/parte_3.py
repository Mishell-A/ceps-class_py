# Funcion Reduce
# Es una función que aplica una función a los elementos de un iterable, de izquierda a derecha, de manera acumulativa.
# Sintaxis: reduce(funcion, iterable)
# Obs: Esta funcion (primer argumento de reduce), debe poseer obligatoriamente dos argumentos (parametros). El primer parametro
# es el acumulador y el segundo es el elemento actual del iterable.

# Obteniendo la suma de los elementos de una lista
# Importamos la función reduce del modulo functools porque reduce ya no es una función integrada en Python 3

# Primera solución: Sin usar reduce
# Definimos la lista de números

lista = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
acumulador = 0

for element in lista:
    acumulador += element
    
print("Suma de los elementos de la lista (sin reduce):", acumulador)

# Segunda solución: Usando reduce
def func_suma(acumulador = 0, elemento = 0):
    return acumulador + elemento

from functools import reduce

resultado = reduce(func_suma, lista)

print("Suma de los elementos de la lista (con reduce):", resultado)

# Tambien podemos reducir el código anterior usando una función lambda
resultado3 = reduce(lambda acumulador = 0, elemento = 0 : acumulador + elemento, lista)

print("Suma de los elementos de la lista (con reduce y función lambda):", resultado3)

# Ejemplo 2
# Concatenar los elementos de una lista de strings
# Definimos la lista de strings

strings = ["Hola", "mundo", "!", "como", "estás"]

resultadoNuevo = reduce(lambda acumulador = "", elementos = "" : acumulador + " " +elementos, strings)

print("Concatenación de los elementos de la lista (con reduce y función lambda):", resultadoNuevo)