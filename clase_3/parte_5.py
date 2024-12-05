# Calculemos el IMC
# El usuario ingresará su peso y su altura

peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
imc = peso/(altura**2)

# Usar una estructura de decisión para determinar si el usuario tiene un peso saludable
if (imc >= 40):
    print("Usted tiene obesidad tipo III")
elif (imc >= 35):
    print("Usted tiene obesidad tipo II")
elif (imc >= 30):
    print("Usted tiene obesidad tipo I")
elif (imc >= 25):
    print("Usted tiene sobrepeso")
elif (imc >= 18.5):
    print("Usted tiene un peso saludable")
else:
    print("Usted tiene muy bajo peso")
