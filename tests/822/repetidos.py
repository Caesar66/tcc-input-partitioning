def repetidos(l):
    '''retorna o n ́umero de vezes que um elemento da lista eh igual ao anterior
    list -> n'''
    i=1
    cont=0
    while i<len(l):
        if l[i]==l[i-1]:
            cont+=1
        i+=1
    return cont
