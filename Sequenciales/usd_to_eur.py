# Conversión de Monedas con Variación: 
# Escribe un programa que convierta una cantidad de dólares a euros, pero que permita ingresar la tasa de cambio actual. 


factor=float(input('Ingrese a cuanto equivale 1 dolar en euros: '))
dolares = float(input('Ingrese su cantidad de dolares: '))
print(f'Su cantidad en euros es: {dolares*factor} euros')