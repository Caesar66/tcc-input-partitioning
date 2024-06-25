import pytest
import importlib

test_cases = [
	('Está na sala, penteando o cabelo, disse-me; vá devagarzinho para lhe pregar um susto.', 14),
	('Capitu confessou-me um dia que esta razão acendeu nela o desejo de o saber.', 14),
	('Foi pelas festas da Coroação.', 5),
	('Eram de vária espécie, explicáveis e inexplicáveis, assim úteis como inúteis, umas graves, outras frívolas; gostava de saber tudo.', 19),
	('Mas, não tendo ela rudimento algum de arte, e havendo feito aquilo de memória em poucos minutos, achei que era obra de muito merecimento; descontai-me a idade e a simpatia.', 30)
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_quant_palavras(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.quant_palavras(frase) == output
