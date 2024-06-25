def filtra_pares(t):
    '''fun ̧c~ao que recebe uma tupla contendo 4 valores inteiros e devolve uma tupla contendo os valores pares da tupla original, na mesma ordem
    tup -> tup'''
    pares = ()
    if t[0]%2 == 0:
        pares = pares + (t[0],)
    if t[1]%2 == 0:
        pares = pares + (t[1],)
    if t[2]%2 == 0:
        pares = pares + (t[2],)
    if t[3]%2 == 0:
        pares = pares + (t[3],)
    return pares
