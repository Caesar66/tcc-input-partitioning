def colchao(lista,H,L):
    maior = max(L,H)
    menor = min(L,H)
    if lista[1] > maior:
        return False
    else:
        if lista[0] > menor:
            return False
        else:
            return True
