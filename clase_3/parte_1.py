# La funcion input siempre almacena lo escrito del usuario como un string

# Ejemplo de uso de la funcion input

nombre = input("Escribe tu nombre: ")

# Castear la variable edad deun string a un entero
edad = int(input("Escribe tu edad: "))

#Ejemplo: Ingresar 5 produceso

nom1 = input("Ingrese el nombre del primer producto: ")
nom2 = input("Ingrese el nombre del segundo producto: ")
nom3 = input("Ingrese el nombre del tercer producto: ")
nom4 = input("Ingrese el nombre del cuarto producto: ")
nom5 = input("Ingrese el nombre del quinto producto: ")

prod1 = float(input("Ingrese el peso del primer número: "))
prod2 = float(input("Ingrese el peso del segundo número: "))
prod3 = float(input("Ingrese el peso del tercer número: "))
prod4 = float(input("Ingrese el peso del cuarto número: "))
prod5 = float(input("Ingrese el peso del quinto número: "))

pesoTotal = prod1 + prod2 + prod3 + prod4 + prod5

print("""
    Productos   Pesos
    ---------   --------
    %s          %.3f
    %s          %.3f
    %s          %.3f
    %s          %.3f
    %s          %.3f
    
    Peso total: %.3f
"""%(nom1,prod1,nom2,prod2,nom3,prod3,nom4,prod4,nom5,prod5,pesoTotal))
