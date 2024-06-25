import pytest
import importlib

test_cases = [
	([3, 6, 1], [4, 9, 3], [3, 4, 6, 9, 1, 3]),
	([8, 7, 4], [7, 6, 9], [8, 7, 7, 6, 4, 9]),
	([9, 4, 3], [2, 6, 0], [9, 2, 4, 6, 3, 0]),
	([1, 2, 6], [2, 0, 3], [1, 2, 2, 0, 6, 3]),
	([6, 9, 5], [9, 1, 3], [6, 9, 9, 1, 5, 3]),
	([4, 5, 8], [1, 7, 9], [4, 1, 5, 7, 8, 9]),
	([9, 4, 7], [4, 9, 6], [9, 4, 4, 9, 7, 6]),
	([7, 6, 4], [5, 2, 0], [7, 5, 6, 2, 4, 0]),
	([4, 2, 3], [6, 2, 5], [4, 6, 2, 2, 3, 5]),
	([6, 2, 7], [5, 9, 1], [6, 5, 2, 9, 7, 1])
]

@pytest.mark.parametrize("lista1, lista2, output", test_cases)
def test_intercala(lista1, lista2, output, solution):
	imp = importlib.import_module(solution)
	assert imp.intercala(lista1, lista2) == output
