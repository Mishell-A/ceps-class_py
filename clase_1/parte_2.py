# El módulo matemático: math

# Cargar el módulo matématico asignandole un alias
import math as m

print(round(m.pow(3,2))) 

# Wildcard: conjunto de caracteres especiales que permiten realizar búsquedas más avanzadas o encontrar patrones

# 1. Para imprimir un entero: %i
# 2. Para imprimir un flotante: %f
# 2. Para imprimir un flotante con dos cifras en la aprte decimal: %.2f
# 3. Para imprimir un string: %s

# Ejemplos de uso de wildcard
# Se asigna una variable
x1 = 137

# La estructura es: print("Texto a mostar % wildcard" % variable)

# Imprimir el valor de x1 utilizando el wildcard %i
# Esto se puede utilizar cuando una variable es float pero se quiere mostrar como entero
print("El valor de x1 es: %i" % x1)

# Imprimir el valor de x1 utilizando el wildcard %f
# Esto se puede utilizar cuando una variable es entero pero se quiere mostrar como float
print("El valor de x1 al cuadrado es: %f" % (x1**(0.5)))

# Imprimir el valor de x1 utilizando el wildcard %.2f
print("El valor de x1 al cuadrado es: %.2f" % (x1**(0.5)))

# Imprimir un numero entero y un numero punto flotante (con 3 cifras en la parte decimal)
print("El valor de x1 es: %i \nEl valor de x1 al cuadrado es :  %.3f" %(x1, x1**(0.5)))


# Uso del docstring con la funcion print
# Se puede utilizar el docstring para imprimir un texto largo
# Se utiliza triple comilla doble, y se puede utilizar saltos de linea 
# Ejemplo con la formula de Coulomb
k = 9 * (10 ** 9)  # Constante de Coulomb en N·m^2/C^2

#Definimos las cargas(C)
q1 = 2 * (10 ** (-6))
q2 = 3 * (10 ** (-9))

#Definimos la distancia entre los dos puntos(d)
d = 12.8 * (10**-2)

#Calculamos la fuerza de Coulomb con la formula
fuerza = (k * q1 * q2) / (d ** 2)

print("""
Fuerza de Coulomb
=================

Entradas:
    q1: %.13f
    q2: %.13f
    d: %.5f
    k : %i

Fuerza Eléctrica: %f
""" %(q1,q2,d,k,fuerza))