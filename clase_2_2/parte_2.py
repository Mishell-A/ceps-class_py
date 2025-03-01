# Sintaxis 
# filter(funcion, iterable)

# Busquemos obtener los elementos mayores a 5 en una tupla

def mayor_a_cinco(numero):
    # Devuelve True si el número es mayor a 5
    return numero > 5

# Definamos la tupla

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Filtramos la tupla utilizando la función mayor_a_cinco
# Observar que el resultado de filter puede 
# ser convertido a una lista o una tupla según sea necesario
filtrado = tuple(filter(mayor_a_cinco, tupla))
filtrado2 = list(filter(mayor_a_cinco, tupla))

print("""
      
      Resultado:
      
      Como tupla: %s
      Como lista: %s
      
      """ %(filtrado,filtrado2))

# Busquemos reducir nuestro codigo usando una funcion lambda
resultado = tuple(filter(lambda x: x > 5, tupla))

print("Resultado con función lambda:", resultado) #Es lo mismo pero con menos lineas de código

# Usemos filter para seleccionar los numeros pares de una lista

# Lista de números

lista = [123, 456, 789, 101, 112, 131, 141, 151, 161, 171, 181, 191, 202]
pares = list(filter(lambda x : x % 2 == 0,lista))

print("Números pares de la lista:", pares)