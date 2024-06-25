import pytest
import importlib

test_cases = [
	([4, 9, 10, 15], 18, [4, 9, 10, 15, 18]),
	([1, 4, 18], 6, [1, 4, 6, 18]),
	([7, 9, 18, 19], 17, [7, 9, 17, 18, 19]),
	([16, 18], 11, [11, 16, 18]),
	([3, 16, 18], 6, [3, 6, 16, 18]),
	([15, 16], 6, [6, 15, 16]),
	([2, 12], 8, [2, 8, 12]),
	([3, 11], 12, [3, 11, 12]),
	([3, 9, 15], 19, [3, 9, 15, 19]),
	([7, 17], 16, [7, 16, 17])
]

@pytest.mark.parametrize("lista_numero, n, output", test_cases)
def test_insere(lista_numero, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.insere(lista_numero, n) == output
