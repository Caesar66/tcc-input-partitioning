def posLetra(frase,letra,ocorrencia):
    '''retorna em que posi ̧c~ao da string a ocorr^encia desejada da letra est ́a.
    str,str,int -> int'''
    pos = 0
    contador = 0
    while pos < len(frase):
        if frase[pos] == letra:
            contador = contador + 1
        if contador == ocorrencia:
            return pos
        pos = pos + 1
    return -1
    
#test_cases = [
#    ("e quanto valia cada sest\u00e9rcio?", "s", 3),
#    ("tio cosme ensinou-lhe gam\u00e3o", "s", 1),
#    ("nascera muito depois daquelas festas c\u00e9lebres", "e", 1),
#    ["que fazia tudo", "e", 1],
#    ["tu quoque brute?", "t", 1],
#    ["as curiosidades de capitu d\u00e3o para um cap\u00edtulo", "p", 4],
#    ["ficou muito tempo com a cara virada para ele", "f", 1],
#    ["conte-me as festas da coroa\u00e7\u00e3o", "e", 1],
#    ["foi pelas festas da coroa\u00e7\u00e3o", "s", 4]
#]
#
#for test in test_cases:
#	print(f'(\'{test[0]}\', \'{test[1]}\', {test[2]}, {posLetra(test[0], test[1], test[2])}),')
