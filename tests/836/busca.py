def busca(setor, matriz):
    '''retorna os dados dos funcionarios de setor
    list -> list'''
    encontrados = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            encontrados.append([matriz[i][0],matriz[i][1],matriz[i][3]])
    return encontrados
    
#test_cases = [
#    ('Desenvolvimento', ["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"], ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"] ),   
#    ('RH', [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"], ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]] ),
#    ('Contabilidade', [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"], ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]] )
#]
#
#for test in test_cases:
#	print(busca(test[0], test[1]))
