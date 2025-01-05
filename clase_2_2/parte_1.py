# Manipulación de colecciones (ITERABLES)

# Función map
# Nos permite aplicar una función sobre cada uno de los elementos de una colección (listas y tuplas)

# Estructura de la función map
# map(funcion_a_aplicar, objero_iterable)

# Ejemplito 
# Obtener el cuadrado de todos los elementos de una lista de números
# Usando la función map
# Definimos la lista de números (objeto iterable)

numbers = [1, 2, 3, 4, 5]

# Definimos la función que se aplicará a cada elemento

def cuadrado(x):
    return x**2

# Aplicamos la función map a la lista de números y convertimos el resultado de tipo map a una lista
Titulo1 = "Usando función normal"
resultado = list(map(cuadrado, numbers))

print("""
    %s
    ------------------
    %s
    """ %(Titulo1, resultado))

# Reduzcamos el código anterior usando una función lambda
Titulo = "Usando función lambda"
resultado2 = list(map(lambda e:e*e, numbers))
print("""
    %s
    ------------------
    %s
    """ %(Titulo, resultado2))

#Jemplo 2
# Observar lo siguiente: map tambien puede ser utilizado con funciones de mas de una
# argumento y mas de una lista

# Importemos el modulo math
import math as m
# Recordemos a la funcion pow(a,b) = a**b

ListaBase = [12,0.5,8,3.6]
ListaExpon = [-1,-2,0.5,3.9]

# Cada i-esimo elemnto de Lista base debe ser elebado por 
# cada i-esimo elemento de ListaExpon

# Estructura de la función map
# map(funcion_a_aplicar, objero_iterable1, objero_iterable2)

resultado3 = list(map(pow,ListaBase,ListaExpon))
print("""
    
    Primer resultado: %.3f
    Segundo resultado: %i
    Tercer resultado: %i
    Cuarto resultado: %.2f
    Lista completa: %s

"""%(resultado3[0],resultado3[1],resultado3[2],resultado3[3],resultado3))