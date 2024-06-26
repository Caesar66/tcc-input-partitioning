import pytest
import importlib

test_cases = [
	([1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7], 6),
	([29, 29, 25, 15, 9, 17, 17, 24, 7, 22, 11, 16, 21, 21, 18, 28, 14, 14], 4),
	([12, 12, 29, 29, 19], 2),
	([16, 19, 3, 3, 12, 14, 21, 25, 24, 24, 23, 23, 5, 13, 10, 9, 27, 27, 2, 2], 5),
	([2, 1, 1, 4, 11, 16, 7, 7, 28, 28, 14, 14, 13, 13, 20, 3, 3, 24, 21, 27, 27, 29, 10, 10], 8),
	([13, 3, 3, 23, 5, 5, 12], 2),
	([5, 5, 21, 21], 2),
	([17, 10, 16, 28, 19, 15, 11, 22, 1, 2, 26, 6, 27, 8, 18, 21, 21, 9, 12, 3], 1),
	([5, 1, 25, 25], 1),
	([10, 23, 23, 27, 27, 9, 9, 6, 6, 29], 4),
	([4, 26, 11, 11, 23, 19, 28, 5, 20, 10], 1),
	([25, 20, 3, 6, 26, 7, 27, 5, 5, 12, 22, 17, 17, 24, 16], 2),
	([4, 4, 10, 9, 9, 11, 11, 24, 23], 3),
	([27, 27, 2, 2, 15, 15, 4, 28, 28, 20, 20, 21, 14, 17, 25, 25], 6),
	([20, 20, 1, 29, 26, 26, 7, 7], 3),
	([24, 14, 9, 29, 5, 13, 27, 22, 8, 18, 18, 15, 12, 12], 2)
]

@pytest.mark.parametrize("lista_numero, output", test_cases)

def test_repetidos(lista_numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.repetidos(lista_numero) == output
