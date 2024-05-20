# Función para Calcular Potencia con Validación: 
# Implementa una función que calcule la potencia de un número dado una base y un exponente, 
# validando que los parámetros sean números enteros. 

def potencia(base, exponente):
    i=1
    resultado=1
    if(exponente>=0):
        while i<=exponente:
            resultado *= base
            i+=1
        return resultado
    else:
        while i>exponente:
            resultado/=base
            i-=1
        return resultado

flag = True

while flag:
    base = input('Ingrese la base de la potenciacion: ')
    exponente = input('Ingrese el exponente de la potencia: ')
    if (base.isdigit() or base.lstrip('-').isdigit()) and (exponente.isdigit() or exponente.lstrip('-').isdigit()):
        print(f'{base}^{exponente} = {potencia(int(base), int(exponente))}')
        flag = False
    else:
        print(f'La base {base} o el exponente {exponente} no son enteros verifiquen que lo sean')
