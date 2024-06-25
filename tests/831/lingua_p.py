def lingua_p(palavra):
    '''traduz palavra da lingua portuguesa na l ́ıngua do P.
    str --> str'''
    
    palavra = str.lower(palavra)
    traduzida = ''
    
    for c in palavra:
        traduzida = traduzida + c
        if c in 'aeiouáàãâéêííóôõú':
            traduzida = traduzida + 'p' + c
    return traduzida
