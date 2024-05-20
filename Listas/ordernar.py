# Ordenación de Lista sin Función de Ordenamiento: 
# Implementa un algoritmo para ordenar una lista de números sin usar la función de ordenamiento incorporada.

from entradas import lista_random

def ordenar_lista(lista):
    n=len(lista)
    for i in range(n-1):
        cambio = False
        for j in range(0,n-i-1):
            if(lista[j]>lista[j+1]):
                lista[j],lista[j+1]=lista[j+1],lista[j]
                cambio = True            
        if not cambio: return

lista = lista_random(10,100)
print(lista)
ordenar_lista(lista)
print(lista)
