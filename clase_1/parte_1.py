#Los comentarios se pueden hacer con el simbolo de hashtag
#Los nombres de las variables deben guardar relacion con el contenido de la variable

#Nota: La funcion de ** es para elevar un numero al numero que le sigue
#Formula de coulomb

k = 9 * (10 ** 9)  # Constante de Coulomb en N·m^2/C^2

#Definimos las cargas(C)
q1 = 2 * (10 ** (-6))
q2 = 3 * (10 ** (-9))

#Definimos la distancia entre los dos puntos(d)
d = 12.8 * (10**-2)

#Calculamos la fuerza de Coulomb con la formula
fuerza = (k * q1 * q2) / (d ** 2)

print(f"La fuerza electrica entre las dos cargas es de: {fuerza}")


#Division entera D = d * q + r
# // : resultado de la division, sale un resultado entero (cociente)
# / : resultado de la division, sale un resultado decimal (cociente)
# % : residuo de la division

# Se define el dividendo (D)
d = 2024

# Se define el divisor (d)

d_divisor = 100

# Se calcula el cociente (q)

q = d // d_divisor

# Se calcula el residuo (r)

r = d % d_divisor

print(f"El cociente es: {q} \nEl residuo es: {r}")

# Operadores de comparacion
# == : igualdad
# != : desigualdad
# > : mayor que
# < : menor que
# >= : mayor o igual que
# <= : menor o igual que

# Operadores logicos	
# and : y
# or : o
# not : negacion




