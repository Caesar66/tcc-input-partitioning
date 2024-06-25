def conta_numero(numero,matriz):
    '''conta quantas vezes numero aparece na matriz.
    list,int -> int'''
    qtd = 0
    for linha in matriz:
        qtd += list.count(linha,numero)
    return qtd
