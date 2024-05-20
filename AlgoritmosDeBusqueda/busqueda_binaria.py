from entradas import lista

def busqueda_binaria(lista, objetivo):
    lista.sort()
    l_inferior = 0
    l_superior = len(lista)-1
    
    while l_inferior<=l_superior:
        mitad_intervalo = ((l_superior-l_inferior)//2) + l_inferior
        print(lista[mitad_intervalo] == objetivo)
        if lista[mitad_intervalo] == objetivo:
            return (mitad_intervalo,lista.index(mitad_intervalo))
        elif (objetivo < lista[mitad_intervalo]):
            l_superior = mitad_intervalo-1
        else:
            l_inferior = mitad_intervalo+1
    return f"El objetivo {objetivo} no fue encontrado en la lista {lista}"

print(busqueda_binaria(lista, 5))