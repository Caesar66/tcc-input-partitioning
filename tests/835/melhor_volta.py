def melhor_volta(matriz):
    '''receba como entrada uma matriz 6 x 10 com os tempos em segundos
    dos corredores em cada volta na pista de kart.
    Retornar o indice da melhor volta, o tempo e que volta.
    list -> tuple(int,float,int)'''
    menores = []
    for linha in matriz:
        menores.append(min(linha))
    menor = min(menores)
    corredor = list.index(menores,menor)
    volta = list.index(matriz[corredor],menor)
    return corredor+1,menor,volta+1
    
#test_cases = [
#    ([[23, 93, 29, 89, 91, 4, 99, 55, 51, 50], [13, 87, 67, 84, 54, 83, 24, 60, 92, 56], [65, 94, 28, 12, 96, 36, 88, 95, 63, 21], [58, 8, 10, 32, 47, 33, 1, 14, 6, 80], [53, 68, 61, 9, 62, 19, 81, 34, 90, 64], [5, 76, 73, 17, 35, 40, 31, 37, 100, 57]], ),
#    ([[19, 40, 14, 23, 72, 26, 93, 78, 21, 71], [18, 41, 64, 13, 85, 66, 94, 17, 49, 2], [86, 73, 75, 9, 8, 11, 65, 79, 46, 3], [4, 39, 58, 61, 84, 55, 1, 5, 70, 63], [67, 6, 10, 33, 12, 48, 87, 74, 56, 7], [68, 62, 47, 15, 76, 34, 16, 42, 81, 20]], ),
#    ([[92, 31, 42, 82, 50, 93, 94, 16, 95, 21], [8, 29, 34, 45, 74, 63, 19, 64, 98, 4], [77, 49, 22, 81, 25, 58, 75, 70, 5, 1], [83, 85, 13, 78, 68, 53, 17, 99, 35, 36], [30, 24, 37, 76, 40, 84, 67, 79, 65, 11], [26, 97, 3, 41, 66, 9, 69, 46, 43, 2]], ),
#    ([[41, 55, 77, 56, 97, 68, 17, 14, 8, 19], [20, 22, 29, 61, 33, 30, 6, 83, 65, 66], [28, 86, 78, 16, 7, 99, 47, 34, 42, 46], [92, 12, 15, 57, 54, 21, 18, 23, 76, 45], [80, 24, 43, 25, 3, 58, 93, 62, 26, 67], [40, 35, 48, 94, 13, 9, 82, 73, 87, 49]], )
#]
#
#for test in test_cases:
#	print(melhor_volta(test[0]))
