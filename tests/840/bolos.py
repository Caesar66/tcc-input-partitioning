def bolos(a,b,c):
    ''' Funcao que calcula quantidade exata de bolos que se consegue fazer
    a - xicaras de farinha; b - num ovos; c - colheres de leite'''
    return min((a//2),(b//3),(c//5))
