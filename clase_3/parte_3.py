# Ejemplo 2:
# Utilice la formula de Heron para calcular el area de un triangulo
# Con los siguientes requerimientos:
# Dos de sus lados son ingresados por el usuario
# El tercer lado lo genera python con la funcion randint del modulo random
# Recordar que el lado 1 debe ser menor que el lado 2

import random as rnd

# Pedir los lados del triangulo al usuario

lado1 = int(input("Ingrese el primer lado del triangulo: "))
lado2 = int(input("Ingrese el segundo lado del triangulo: "))

# Generar el tercer lado del triangulo
lado3 = rnd.randint(lado1,lado2)

p = (lado1 + lado2 + lado3)/2

area = (p*(p-lado1)*(p-lado2)*(p-lado3))**(0.5)

print("""
      Lados del triangulo:
      
        Lado 1: %i
        Lado 2: %i
        Lado 3: %i
        
        Semiperimetro: %i
        
        Area del triangulo: %.2f
"""%(lado1,lado2,lado3,p,area))
