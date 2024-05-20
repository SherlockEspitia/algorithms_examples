# Generación de Serie Geométrica: 
# Genera y muestra los primeros n términos de una serie geométrica dada la razón y el primer término. 

# G= Sumatorio de A*r^n 

valor_i = float(input('Ingrese el valor inicial: '))
razon = float(input('Ingrese la razon: '))

n = int(input('Ingrese los terminos que quiere vizualizar: '))

for i in range(n):
    print(valor_i*(razon**i))