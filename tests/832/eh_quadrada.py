def eh_quadrada(matriz):
    '''returna True se a matriz  ́e quadrada
    list -> bool'''
    if len(matriz)!=0:
        return len(matriz)==len(matriz[0])
    else:
        return True
