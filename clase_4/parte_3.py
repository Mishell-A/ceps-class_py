import random as rnd
# Vamos a pdir a python que genere 10000 numeros en el intevalo de [1,999]
# que cuente cuantos de estos numeros son multiplos de 3

sum_multrece_bucle = 0

# Iteramos 100 veces para generar 10000 numeros aleatorios y contar los multiplos de 13
# en cada iteracion sumamos la cantidad de multiplos de 13
for i in range (100):
    mult = 0
    for n in range(10000):
        #range(10000) y range(0, 10000) hacen lo mismo, es decir, 
        # ambos generan una secuencia de números que va desde 0 hasta 9999.(genera 10000 números)
        # La diferencia es simplemente en la forma de escribirlo.
        num = rnd.randrange(1,999)
        if (num % 13 == 0):
            mult += 1
            
    sum_multrece_bucle += mult
media_aritmetica = sum_multrece_bucle/100

print("""
    Resultados:
    ----------------------------------------------------------------------------------
    Multiplos de 13 en la iteracion de 100 vueltas es: %i
    
    La media artimetica del total de multiplos de 13 en 100 iteraciones es: %.2f
""" %(sum_multrece_bucle, media_aritmetica))            
