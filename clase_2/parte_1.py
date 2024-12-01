# Naturaleza de los strings o cadena de caracteres
# En python los indices empiezan en cero

ejemplo = "Uso de strings"

# Primer caracter del ejemplo
print(ejemplo[0]) # U

# Pero si se lee de derecha (<-) a izquierda el indice empieza en -1 y van disminuyendo de -1 en -1

# El ultimo caracter del ejemplo
print(ejemplo[-1]) # s

# El penultimo caracter del ejemplo
print(ejemplo[-2]) # g

# Si se quiere mostrar un numero de caracteres de un string se puede hacer con el siguiente formato

# Ejemplo: quiero mostrar los primeros 3 caracteres
# El formato es [inicio:fin]
# El indice final no se incluye

print(ejemplo[0:3])

# Ejemplo: quiero mostrar los ultimos 3 caracteres

print(ejemplo[-3:])

# Funcion len : Devuelve la longitud de un string

print(len(ejemplo))

# Se puede asignar la longitud de un string a una variable
num_elem_ej = len(ejemplo)


# Usar replace para reemplazar un caracter por otro
print(ejemplo.replace(" ",""))

# Usar count para contar cuantas veces aparece un caracter en un string
print(ejemplo.count("s"))