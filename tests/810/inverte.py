def sempontuacao(frase):
    '''a frase sem pontua ̧c~ao
    str -> str'''
    sem_pontos = str.replace(str.replace(str.replace(frase,","," "),"."," "),"..."," ")
    sem_pontos2= str.replace(str.replace(str.replace(sem_pontos,"!"," "),"?"," "),";"," ")
    return str.replace(str.replace(sem_pontos2, ":", " "), "-"," ")

def inverte(frase):
    lista = str.split(sempontuacao(str.lower(frase)))
    return str.join(" ",lista[::-1])
