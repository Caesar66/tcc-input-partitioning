test_str = '''	806 - Detectando colisões com tuplas	[[1, 4, 9, 7], [8, 7, 9, 8]]
	806 - Detectando colisões com tuplas	[[1, 5, 4, 8], [5, 6, 8, 9]]
	806 - Detectando colisões com tuplas	[[5, 5, 7, 7], [6, 3, 8, 8]]
	806 - Detectando colisões com tuplas	[[4, 8, 9, 9], [2, 1, 9, 5]]
	806 - Detectando colisões com tuplas	[[6, 5, 8, 7], [6, 2, 7, 5]]'''
	
tests = []
for line in test_str.split('\n'):
	elements = line.split('[', maxsplit=1)
	tests.append(eval('[' + elements[-1]))

def main(test):
	def colisao(ret1,ret2):
		# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
		x_esq1, y_inf1, x_dir1, y_sup1 = ret1
		x_esq2, y_inf2, x_dir2, y_sup2 = ret2
		# segunda etapa - calculo do resultado
		# se o extremo mais a direita de um retangulo esta antes do
		# extremo mais a esquerda do outro nao tem como ter batida
		if x_dir2 < x_esq1 or x_dir1 < x_esq2:
		    return False
		# se o extremo mais acima de um retangulo esta abaixo do
		# extremo mais abaixo do outro nao tem como ter batida
		if y_sup2 < y_inf1 or y_sup1 < y_inf2:
		    return False
		# se chegou aqui eh porque tem batida
		return True
	return colisao(*test)

for test in tests:
	result = main(test)
	str_ = '('
	for arg in test:
		if type(arg) == str:
			str_ = str_ + '\'' + str(arg) + '\'' + ', '
		else:
			str_ = str_ + str(arg) + ', '
	if type(result) == str:	
		print(str_ + f'\'{result}\'),')
	else:
		print(str_ + f'{result}),')
	
