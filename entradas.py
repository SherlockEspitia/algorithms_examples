from random import random as rand

def lista_random(cantidad_de_valores=10, rango_valores=10):

    lista = []

    for x in range(cantidad_de_valores):
        lista.append(int(rango_valores*rand()+ 1))
    
    return lista

lista = lista_random()