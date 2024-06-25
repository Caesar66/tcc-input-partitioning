import pytest
import importlib

test_cases = [
	([1, 3, 4, 5], 2),
	([2, 3, 4, 5], 1),
	([1, 2, 4], 3),
	([1, 2, 3, 4, 5, 7, 8], 6),
	([1], 2),
	([1, 2, 3, 5, 6, 7], 4),
	([1, 2, 4], 3),
	([1, 2, 3], 4),
	([1, 2], 3),
	([2], 1),
	([1, 2, 3, 4], 5)
]

@pytest.mark.parametrize("lista_numero, output", test_cases)

def test_faltante(lista_numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.faltante(lista_numero) == output
