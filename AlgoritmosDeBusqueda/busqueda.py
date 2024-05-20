from entradas import lista

def busqueda_numero(lista, objetivo):
    for index, item in enumerate(lista):
        if(item == objetivo):
            return (index+1, item)
    return f"No hay ningun valor {objetivo} en la lista: {lista}"
        
print(busqueda_numero(lista, 5))