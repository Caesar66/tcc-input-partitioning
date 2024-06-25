import math
def carros(passageiros,capacidade=5):
    '''numero de carros necessarios para transportar os passageiros; int, int -> int'''
    return math.ceil(passageiros/capacidade)
