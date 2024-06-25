import math
from math import*
def carros(pas,cap=5):
    """Pede o número de pessoas que vão viajar
    e a capacidade de passageiros por veículo,
    assumindo um valor default de 5, e calcula
    o número mínimo de veículos para a viagem,
    assumindo que todos sejam iguais"""
    veiculos=pas/cap
    return math.ceil(veiculos)