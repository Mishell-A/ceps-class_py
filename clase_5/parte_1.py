# TUPLAS

# Objetos iterables que son inmutables
# Se definen con paréntesis ()

t1 = (12,15,9,21)

# Acceder a un elemento por índice

print(t1[0])  # Output: 12
print(t1[-1])  # Output: 21


# DICCIONARIOS
# Son objetos iterables que contienen una llave y un valor
# Se definen con llaves {}
d1 = {}

# Cada elemento de un dicionario se define con un par llave : valor
d2 = {"nombre": "Juan", "edad": 25, "ciudad": "Lima"}
print(d2)

# Acceder a un valor por su llave
print(d2["nombre"])  # Output: Juan
print(d2["edad"])  # Output: 25

# Metodos de los diccionarios
# 1. get(): Devuelve el valor de una llave
print(d2.get("nombre"))  # Output: Juan

# 2. items(): Devuelve una lista de tuplas con las llaves y los valores
print(d2.items())  # Output: dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'Lima')])

# 3. keys(): Devuelve una lista con las llaves
print(d2.keys())  # Output: dict_keys(['nombre', 'edad', 'ciudad'])

# 4. values(): Devuelve una lista con los valores
print(d2.values())  # Output: dict_values(['Juan', 25, 'Lima'])

# 5. update(): Actualiza un diccionario con los elementos de otro
d3 = {"nombre": "Maria", "edad": 30, "ciudad": "Arequipa"}
d2.update(d3)
print(d2)  # Output: {'nombre': 'Maria', 'edad': 30, 'ciudad': 'Arequipa'}

# 6. pop(): Elimina un elemento del diccionario por su llave
d2.pop("ciudad")
print(d2)  # Output: {'nombre': 'Maria', 'edad': 30}

# 7. clear(): Elimina todos los elementos del diccionario

d2.clear()
print(d2)  # Output: {}

# Añadir un elemento al diccionario
d2["ciudad"] = "Lima"

print(d2)  # Output: {'nombre': 'Maria', 'edad': 30, 'ciudad': 'Lima'}

# fromkeys(): Crea un diccionario con las llaves y un valor por defecto
# Definamos una lista con elementos enteros aleatorios
# Estos elementos serán las llaves del diccionario

import random as rnd

# Numero de elementos a generar
n = int(input("Ingrese el numero de elementos a generar: "))

llaves = []

for k in range(n):
    llaves.append(rnd.randint(0,20000))
    
# Definamos un diccionario con llaves provenientes de la lista "llaves"

d3 = dict.fromkeys(llaves, "Valor por defecto")

print(d3)

# Modificamos los valores correpsondientes
# Definamos una funcion que me devuelva un carcter aleatorio
def MakeChar():
    abcdario = "abcdefghijklmnopqrstuvwxyz"
    return abcdario[rnd.randint(0,25)]

for elemento in llaves:
    d3[elemento] = MakeChar()

print(d3)