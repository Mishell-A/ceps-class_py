# Ejemplo: 
# Dados los puntos P = (a1,b1) y Q = (t1,r1)
# Los cuatro pntos son generados utilizando la funcion random
# Calcular las coordenadas de punto medio (M)
import random as rnd

a1 = rnd.random()
b1 = rnd.random()
t1 = rnd.random()
r1 = rnd.random()

p_medio_x = ((a1+t1)/2)
p_medio_y = ((b1+r1)/2)

print("""
    Puntos:
    A = (%f,%f)
    B = (%f,%f)
    
    Coordenadas del punto medio:
    Pm  = (%f,%f)
"""%(a1,b1,t1,r1,p_medio_x,p_medio_y))