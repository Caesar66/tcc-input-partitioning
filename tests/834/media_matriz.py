def media_matriz(matriz):
    '''retorna a m ́edia dos numeros da matriz.
    list -> float'''
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    media = float(soma)/(len(matriz)*len(matriz[0]))
    return round(media,2)
