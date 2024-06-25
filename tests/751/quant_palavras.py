def quant_palavras(frase):
    '''retorne o n ́umero de palavras de frase. str -> int'''
    words = frase.split()
    return len(words)
    
print(quant_palavras("O Cais-115# é o     primeiro! "))
