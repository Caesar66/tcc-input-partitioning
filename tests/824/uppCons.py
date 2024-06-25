def uppCons(frase):
    '''Funcao que recebe uma frase e transforma as
    todas as suas consoantes em maiúsculas
    str -> str'''
    frase_tratada = ''
    i=0
    while i<len(frase):
        caractere=frase[i]
        if caractere in 'bcdfghjklmnpqrstvwxyzç':
            caractere = str.upper(caractere)
        frase_tratada = frase_tratada + caractere
        i=i+1
    return frase_tratada
