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

def acima_da_media(notas):
    '''retorne uma lista com as notas que ficaram acima da m ́edia.
    list -> list'''
    media=sum(notas)/len(notas)
    return maiores(notas,media)
