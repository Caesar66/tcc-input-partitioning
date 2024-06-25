import pytest
import importlib

test_cases = [
    ([2,3,4], 1),
    ([1,3,4,5], 2),
    ([1,2,3], 4),
    ([2,4,1,3], 5),
    ([3,5,4,1], 2),
    ([3,2,4,5], 1)
]

@pytest.mark.parametrize("lista_numero, output", test_cases)

def test_faltante(lista_numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.faltante(lista_numero) == output
