def freq_palavras(frase):
    '''retorna dicionario com o numero de vezes de cada palavra na frase
    str -> dici'''
    dic = {}
    lista = frase.split()
    for palavra in lista:
        if palavra in dic:
            dic[palavra] += 1
        else:
            dic[palavra] = 1
    return dic
