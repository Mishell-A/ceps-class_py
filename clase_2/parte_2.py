# Ejemplo 1

#Considere una lista de compras y su precio unitario

# 1.5 kg de arroz
# 18 litros de agua
# 6 latas de atún
# 12 kg de azucar
# 3 detergentes de 1kg

#Los precios unitarios son:

# 1kg de arroz a 4.2
# 1 litro de agua a 2.5
# 1 lata de atún a 5.9
# 1kg de azucar a 5.2
# 1 detergente a 4.6

#Calcular el total de la compra

# Entradas del programa

arroz = 1.5
agua = 18
atun = 6
azucar = 12
detergente = 3

p_arroz = 4.2
p_agua = 2.5
p_atun = 6.9
p_azucar = 5.2
p_detergente = 4.6

# Proceso

total_arroz = arroz * p_arroz
total_agua = agua * p_agua
total_atun = atun * p_atun
total_azucar = azucar * p_azucar
total_detergente = detergente * p_detergente

# Salida

costo_total = total_arroz + total_agua + total_atun + total_azucar + total_detergente

# Mostrar los resultados

print("""
Lista de compras
----------------

Fecha: 01/12/2024

El costo total de la compra es : % i

""" % (costo_total))

