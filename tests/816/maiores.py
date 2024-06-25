def maiores(lista,n):
    '''elementos da lista original maiores que n.
    lista, int/float -> lista'''
    lista = lista+[n]
    list.sort(lista)
    list.reverse(lista)
    indice=list.index(lista,n)
    sublista=lista[:indice]
    list.reverse(sublista)
    return sublista
