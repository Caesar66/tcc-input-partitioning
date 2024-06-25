import pytest
import importlib

test_cases = [
    ([], 0),
    ([1, 2, 4, -5.5, 10], 0),
    ([2, 2, 4, 10, 12], 1),
    ([-1.1, 1.1, 2.2, 2.5, 3.1, 3.1], 1),
    ([1.1, 1.1, 1.1, 1.1], 3),
    ([-1, 2, 3, 3, 4, 5, 5, 6, -7], 2),
    ([-1, -1, -1, -1, -1, -1], 5)
]

@pytest.mark.parametrize("lista_numero, output", test_cases)

def test_repetidos(lista_numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.repetidos(lista_numero) == output
