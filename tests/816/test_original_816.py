import pytest
import importlib

test_cases = [
	([16, 6, 13, 3, 7, 18, 15], 2, [3, 6, 7, 13, 15, 16, 18]),
	([2, 16, 10, 14, 1, 12, 18, 5], 11, [12, 14, 16, 18]),
	([8, 14, 15, 5, 11, 7, 2, 16, 12], 6, [7, 8, 11, 12, 14, 15, 16]),
	([1, 3, 2], 10, []),
	([11], 4, [11]),
	([15, 18, 3, 19, 14, 10], 2, [3, 10, 14, 15, 18, 19]),
	([16, 12, 2, 4, 13, 18, 10, 17, 1], 20, [])
]

@pytest.mark.parametrize("lista, n, output", test_cases)
def test_maiores(lista, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.maiores(lista, n) == output
