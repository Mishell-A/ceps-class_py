cadena = """1.Je t'aime, je te quitte, je t'aime, je te quitte
2.Je taime, je te quitte, je t'aime, je te quitte
3.Je taime, je te quitte, je t'aime, je te quitte
4.Je taime, je te quitte, je t'aime, je te quitte

5.T'es la meilleure chose qui mest arrivée
Mais aussi la pire chose qui mest arrivée
Ce jour où je t'ai rencontrée, jaurais peut-être préféré
Que ce jour ne soit jamais arrivé (arrivé)
La pire des bénédictions
La plus belle des malédictions
De toi, j'devrais m'éloigner
Mais comme dit le dicton
Plutôt qu'être seul, mieux vaut être mal accompagné

Tu sais c'qu'on dit
Sois près d'tes amis l8es plus chers
Mais aussi
Encore plus près d'tes adversaires

Mais ma meilleure ennemie, c'est toi
Fuis-moi, le pire, c'est toi et moi
Mais si tu cherches encore ma voix
Oublie-moi, le pire, c'6est toi et moi

Pourquoi ton prénom me blesse
Quand il se cache juste là dans l'espace?
C'est quelle émotion, la haine
Ou la douceur, 5quand j'entends ton prénom?

Je t'avais dit, "ne regarde pas en arrière"
Le passé qui te suit te fait la guerre

Mais ma meille8ure ennemie, cest toi
Fuis-moi, le pire, cest toi et moi
Mais ma meilleure ennemie, c'est toi
Fuis-moi, le pire, cest toi et moi"""

# Contar cuantos numeros hay en la cadena
# Asignar una varible acumuladora

Num_digitos = 0
for elemento in cadena:
    if(elemento.isdecimal() == True):
        Num_digitos += 1
print("La cantidad de números que aparecen en la cadena es: %i" %Num_digitos)

# Mostrar los numeros que aparecen en la cadena
Digitos = ""
contador = 0
for i in cadena:
    if(i.isdecimal() == True):
        # Isdecimal() es un método que se utiliza para saber si un caracter es un número
        # Se concatena el digito a la cadena Dig: Por ejemplo
        # Dig = "1" -> Dig = "1" + "2" -> Dig = "12"
        Digitos += i
    if (i == "5"):
        contador += 1
print("""
    Los digitos que aparecen en la cadena son: %s
    La cantidad de digitos que aparecen en la cadena es: %i
    La cantidad de veces que el numero 5 aparece en la cadena es: %i
""" %(Digitos,len(Digitos),contador))

# El usuario ingresará un número y se mostrará la cantidad de veces que aparece en la cadena

num = input("Ingrese el número a buscar (0-9): ")
contador = 0
# Buscar el número en la cadena
for i in cadena:
    if i == num:
        contador += 1
        
print("El numero %s aparece %s veces en la cadena" %(num, contador))