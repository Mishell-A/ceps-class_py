# Iterador for

# Ejemplo

cad1 = "Hola 4"

# Identificar si un caracter es un digito o no en una cadena caracteres
# Se itera cada caracter de la cadena y se pregunta si es un digito o no
for i in cad1:
    if(i.isdecimal == True):
        print("Dígito: %s" %i)
    else:
        print("Caracter: %s" %i)
    