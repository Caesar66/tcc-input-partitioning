import pytest
import importlib

test_cases = [
	('Fulaninho chega, funalinho acha que está arrasando.', {'Fulaninho': 1, 'chega,': 1, 'funalinho': 1, 'acha': 1, 'que': 1, 'está': 1, 'arrasando.': 1}),
	('Ando com muitas dúvidas. Ando com muitas angústias. Ando com muitos medos.', {'Ando': 3, 'com': 3, 'muitas': 2, 'dúvidas.': 1, 'angústias.': 1, 'muitos': 1, 'medos.': 1}),
	('Tinha uma pedra no meio do caminho. No meio do caminho tinha uma pedra. (Drummond).', {'Tinha': 1, 'uma': 2, 'pedra': 1, 'no': 1, 'meio': 2, 'do': 2, 'caminho.': 1, 'No': 1, 'caminho': 1, 'tinha': 1, 'pedra.': 1, '(Drummond).': 1}),
	('A voz do povo é a voz de Deus. (ditado popular).', {'A': 1, 'voz': 2, 'do': 1, 'povo': 1, 'é': 1, 'a': 1, 'de': 1, 'Deus.': 1, '(ditado': 1, 'popular).': 1}),
	('Hoje visitei a velha estação de trem. A estação estava coberta de abandono. Porque, hoje, as pessoas parecem não dar bola para construções velhas como essa da estação de trem. Muitas pessoas só querem saber de coisas futuras. Dão bola só para coisas novas.', {'Hoje': 1, 'visitei': 1, 'a': 1, 'velha': 1, 'estação': 3, 'de': 4, 'trem.': 2, 'A': 1, 'estava': 1, 'coberta': 1, 'abandono.': 1, 'Porque,': 1, 'hoje,': 1, 'as': 1, 'pessoas': 2, 'parecem': 1, 'não': 1, 'dar': 1, 'bola': 2, 'para': 2, 'construções': 1, 'velhas': 1, 'como': 1, 'essa': 1, 'da': 1, 'Muitas': 1, 'só': 2, 'querem': 1, 'saber': 1, 'coisas': 2, 'futuras.': 1, 'Dão': 1, 'novas.': 1}),
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_freq_palavras(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.freq_palavras(frase) == output
