import pytest
import importlib

test_cases = [
    ('Desenvolvimento', [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"], ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]], []),
    ('RH', [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"], ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]], [['Juliana Vasconcelos', '465', '(21)3555-4552']]),
    ('Contabilidade', [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"], ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]], [['Adalberto Ferreira', '566', '(21)84564-5248'], ['Flavia Amorim', '565', '(21)2134-4845']])
]

@pytest.mark.parametrize("setor, matriz, output", test_cases)

def test_busca(setor, matriz, output, solution):
	imp = importlib.import_module(solution)
	assert imp.busca(setor, matriz) == output
