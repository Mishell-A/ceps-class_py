# Ejercicio 2: Contar cuantas vocales hay en el siguiente string

ma_Meilleure_Ennemie = """Je t'aime, je te quitte, je t'aime, je te quitte
Je taime, je te quitte, je t'aime, je te quitte
Je taime, je te quitte, je t'aime, je te quitte
Je taime, je te quitte, je t'aime, je te quitte

T'es la meilleure chose qui mest arrivée
Mais aussi la pire chose qui mest arrivée
Ce jour où je t'ai rencontrée, jaurais peut-être préféré
Que ce jour ne soit jamais arrivé (arrivé)
La pire des bénédictions
La plus belle des malédictions
De toi, j'devrais m'éloigner
Mais comme dit le dicton
Plutôt qu'être seul, mieux vaut être mal accompagné

Tu sais c'qu'on dit
Sois près d'tes amis les plus chers
Mais aussi
Encore plus près d'tes adversaires

Mais ma meilleure ennemie, c'est toi
Fuis-moi, le pire, c'est toi et moi
Mais si tu cherches encore ma voix
Oublie-moi, le pire, c'est toi et moi

Pourquoi ton prénom me blesse
Quand il se cache juste là dans l'espace?
C'est quelle émotion, la haine
Ou la douceur, quand j'entends ton prénom?

Je t'avais dit, "ne regarde pas en arrière"
Le passé qui te suit te fait la guerre

Mais ma meilleure ennemie, cest toi
Fuis-moi, le pire, cest toi et moi
Mais ma meilleure ennemie, c'est toi
Fuis-moi, le pire, cest toi et moi"""

# Verificar si es tipo straing: print(type(ma_Meilleure_Ennemie))

# Operaciones
# 1. Pasar todo a minusculas

# Dato: Para pasar un string a minusculas se utiliza el metodo lower() y para pasar a mayusculas se utiliza el metodo upper()
ma_Meilleure_Ennemie.lower()

# 2. Contar cuantas vocales hay en el string

Num_voc_a = ma_Meilleure_Ennemie.count("a") 
Num_voc_e = ma_Meilleure_Ennemie.count("e")
Num_voc_i = ma_Meilleure_Ennemie.count("i")
Num_voc_o = ma_Meilleure_Ennemie.count("o")
Num_voc_u = ma_Meilleure_Ennemie.count("u")

Total_vocal = Num_voc_a + Num_voc_e + Num_voc_i + Num_voc_o + Num_voc_u

print("""
      Detalles:
      
      El número de vocales "a": %i
      El número de vocales "e": %i
      El número de vocales "i": %i
      El número de vocales "o": %i
      El número de vocales "u": %i
      
      El numero total de vocales en el string es: %i
      
      """ %(Num_voc_a,Num_voc_e,Num_voc_i,Num_voc_o,Num_voc_u,Total_vocal))

