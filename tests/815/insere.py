def insere(lista,n):
    '''dada uma lista ordenada (crescente) de n ́umeros inteiros e um n ́umero inteiro n,
    inclua n na posi ̧c~ao correta.
    list,int -> list'''
    lista=lista+[n]
    list.sort(lista)
    return lista
