def intercala(lista1,lista2):
    lista3 = 6*[0]
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3
