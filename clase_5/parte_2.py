# Considere unica y excluisvamente los caracteres de la variable abcedario 
# Cuente el numero de veces que aparece cada uno de estos caracteres en un parrafo
# Almacenando el resultado en un diccionario

abcdario = "abcdefghijklmnopqrstuvwxyz"
parrafo = "Este es un ejemplo de un párrafo que contiene varios caracteres del abecedario."

# Inicializar el diccionario con los caracteres del abecedario y contar ocurrencias
conteo_caracteres = {letra: parrafo.lower().count(letra) for letra in abcdario}

print(conteo_caracteres)
