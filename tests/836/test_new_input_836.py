import pytest
import importlib

test_cases = [
    ('', [], []),
    ('', [["ArthurMoreiraDeAlbuquerque", "0123456789", "", "(11) 99999-9999"]], [["ArthurMoreiraDeAlbuquerque", "0123456789", "(11) 99999-9999"]]),
    ('contabilidade', [["ArthurMoreiraDeAlbuquerque", "0123456789", "Administracao", "(11) 99999-9999"]], []),
    ('setor financeiro', [["ArthurMoreiraDeAlbuquerque", "0123456789", "setor financeiro", "(11) 99999-9999"], ["PedroDaCosta", "0987654321", "setor financeiro", "(11) 22222-2222"]], [["ArthurMoreiraDeAlbuquerque", "0123456789", "(11) 99999-9999"], ["PedroDaCosta", "0987654321", "(11) 22222-2222"]]),
    ('', [["ArthurMoreiraDeAlbuquerque", "0123456789", "", "(11) 99999-9999"], ["PedroDaCosta", "0987654321", "", "(11) 22222-2222"]], [["ArthurMoreiraDeAlbuquerque", "0123456789", "(11) 99999-9999"], ["PedroDaCosta", "0987654321", "(11) 22222-2222"]]),
    ('Manutencao e Compuradores', [["ArthurMoreiraDeAlbuquerque", "0123456789", "setor financeiro", "(11) 99999-9999"], ["PedroDaCosta", "0987654321", "setor financeiro", "(11) 22222-2222"]], []),
    ('RECEPCAO', [["ArthurMoreiraDeAlbuquerque", "0123456789", "RECEPCAO", "(11) 99999-9999"]], [["ArthurMoreiraDeAlbuquerque", "0123456789", "(11) 99999-9999"]]),
    ('manutencao e compuradores', [["ArthurMoreiraDeAlbuquerque", "0123456789", "manutencao e compuradores", "(11) 99999-9999"], ["PedroDaCosta", "0987654321", "setor financeiro", "(11) 22222-2222"]], [["ArthurMoreiraDeAlbuquerque", "0123456789", "(11) 99999-9999"]]),
    ('RECEPCAO', [["ArthurMoreiraDeAlbuquerque", "0123456789", "RECEPCAO", "(11) 99999-9999"], ["PedroDaCosta", "0987654321", "RECEPCAO", "(11) 22222-2222"]], [["ArthurMoreiraDeAlbuquerque", "0123456789", "(11) 99999-9999"],  ["PedroDaCosta", "0987654321", "(11) 22222-2222"]])
]

@pytest.mark.parametrize("setor, matriz, output", test_cases)

def test_busca(setor, matriz, output, solution):
	imp = importlib.import_module(solution)
	assert imp.busca(setor, matriz) == output
