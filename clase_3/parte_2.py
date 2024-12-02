# Ejemplo
# Pida al usuario dos numeros enteros y genere 3 numeros aleatorios usando la funcion gauss del modulo random

import random as rnd

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

# Proceso

x1 = rnd.gauss(num1,num2)
x2 = rnd.gauss(num1,num2)
x3 = rnd.gauss(num1,num2)

# Mostremos los 3 numeros pseudoaleatorios

print("""
    Numeros ingresados:
    
    Número 1: %i
    Número 2: %i
    
    Numeros pseudoaleatorios:
    
    Resultado 1: %f
    Resultado 2: %f
    Resultado 3: %f
"""%(num1,num2,x1,x2,x3))