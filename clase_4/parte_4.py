# Que es una lista y como funciona

# Lista de palabras

frutas = ['manzana', 'pera', 'uva', 'kiwi', 'naranja']

# Para acceder a un elemento de la lista, utilizamos corchetes [] y el índice del elemento

# Por ejemplo, para acceder a la palabra 'manzana' que es el primer elemento de la lista, se hace de la siguiente manera

print(frutas[0])  # Imprime: manzana

# Ahora explica que cosas se pueden hacer con una lista

# 1. Añadir elementos: Para añadir un elemento a la lista, utilizamos el método append()

frutas.append('mango')  # Añade 'mango' al final de la lista

print(frutas)  # Imprime: ['manzana', 'pera', 'uva', 'kiwi', 'naranja', 'mango']

# 2. Eliminar elementos: Para eliminar un elemento de la lista, utilizamos el método remove()

frutas.remove('pera')  # Elimina la palabra 'pera' de la lista

print(frutas)  # Imprime: ['manzana', 'uva', 'kiwi', 'naranja', 'mango']

# 3. Modificar elementos: Para modificar un elemento de la lista, utilizamos el índice del elemento y el nuevo valor

frutas[3] = 'melon'  # Cambia la palabra 'kiwi' por 'melon'

print(frutas)  # Imprime: ['manzana', 'uva', 'melon', 'naranja', 'mango']

# 4. Buscar elementos: Para buscar un elemento en la lista, utilizamos el método index()

print(frutas.index('melon'))  # Imprime: 2

# 5. Ordenar una lista: Para ordenar una lista, utilizamos el método sort()

frutas.sort()  # Ordena la lista en orden alfabético

print(frutas)  # Imprime: ['kiwi', 'manzana', 'melon', 'mango', 'naranja']

# 6. Obtener la longitud de una lista: Para obtener la longitud de una lista, utilizamos el método len()

print(len(frutas))  # Imprime: 5

# pop() es un método que elimina el último elemento de la lista y lo devuelve

print(frutas.pop())  # Imprime: naranja y devuelve 'naranja'

# pop con índice es un método que elimina un elemento de la lista en una posición específica y lo devuelve

print(frutas.pop(0))  # Imprime: mango y devuelve 'mango'

print(frutas)  # Imprime: []

print(frutas)  # Imprime: ['kiwi', 'manzana', 'melon', 'mango']

# reverse() es un método que invierte el orden de los elementos de la lista

frutas.reverse()  # Invierte la lista

print(frutas)  # Imprime: ['mango', 'melon', 'manzana', 'kiwi']

# count() es un método que devuelve el número de veces que aparece un elemento en la lista

print(frutas.count('melon'))  # Imprime: 1

# extend() es un método que añade elementos de otra lista al final de la lista actual

otras_frutas = ['papaya', 'guanábana']

frutas.extend(otras_frutas)  # Añade 'papaya' y 'guanábana' al final de la lista

print(frutas)  # Imprime: ['mango', 'melon', 'manzana', 'kiwi', 'papaya', 'guanábana']

# insert() es un método que añade un elemento en una posición específica de la lista

frutas.insert(2, 'banana')  # Añade 'banana' en la posición 2 de la lista

print(frutas)  # Imprime: ['mango', 'melon', 'banana', 'manzana', 'kiwi', 'papaya', 'guanábana']

# clear() es un método que elimina todos los elementos de la lista

frutas.clear()  # Elimina todos los elementos de la lista

print(frutas)  # Imprime: []

# copy() es un método que devuelve una copia de la lista

copia_frutas = frutas.copy()  # Crea una copia de la lista

print(copia_frutas)  # Imprime: []

# Las listas son mutables, es decir, se pueden cambiar después de ser creadas

