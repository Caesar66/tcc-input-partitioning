import pytest
import importlib

test_cases = [
    ([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]),
    ([[1], [1, 2], (3,)], [1, 2, 3], [[1], 1, [1, 2], 2, (3,), 3]),
    ([1, 2, 3], [[1], [1, 2], (3,)], [1, [1], 2, [1, 2], 3, (3,)]),
    ([[1], [1, 2], (3,)], [[1], [1, 2], (3,)], [[1], [1], [1, 2], [1, 2], (3,), (3,)]),
    ([1, [1, 2], (3,)], [1, [1, 2], (3,)], [1, 1, [1, 2], [1, 2], (3,), (3,)])
]

@pytest.mark.parametrize("lista1, lista2, output", test_cases)
def test_intercala(lista1, lista2, output, solution):
	imp = importlib.import_module(solution)
	assert imp.intercala(lista1, lista2) == output
