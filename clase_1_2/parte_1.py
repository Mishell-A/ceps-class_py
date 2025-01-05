#Usando la palabra reservada lambda
import random as rnd
f1_anonima = lambda w : 0.5*w**(rnd.randint(12,20))

print(f1_anonima(1))

# Otra funcion lambda
suma3 = lambda x,y,z : print(x+y+z)

muestra = suma3(1,2,3)
prueba_listas = suma3([1,2,3],[],[4,5])