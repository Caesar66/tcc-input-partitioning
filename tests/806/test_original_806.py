import pytest
import importlib

test_cases = [
	([1, 4, 9, 7], [8, 7, 9, 8], True),
	([1, 5, 4, 8], [5, 6, 8, 9], False),
	([5, 5, 7, 7], [6, 3, 8, 8], True),
	([4, 8, 9, 9], [2, 1, 9, 5], False),
	([6, 5, 8, 7], [6, 2, 7, 5], True)
]

@pytest.mark.parametrize("tupla1, tupla2, output", test_cases)

def test_colisao(tupla1, tupla2, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colisao(tupla1, tupla2) == output
