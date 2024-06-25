import pytest
import importlib

test_cases = [
	(2, [[3, 4, 5], [6, 7, 8]], 0),
	(0, [], 0),
	(4, [[5, 2], [3, 4], [8, 5]], 1),
	(3, [[9, 6, 1], [1, 9, 3]], 1),
	(5, [[1, 7, 9], [8, 0, 9], [0, 6, 1], [8, 6, 5]], 1),
	(7, [[2, 7]], 1),
	(2, [[9, 4, 9, 4, 0], [6, 3, 6, 3, 6], [7, 2, 0, 1, 6], [2, 0, 6, 5, 3], [4, 7, 6, 4, 4]], 2),
	(0, [[8, 1, 4, 8, 2], [4, 6, 4, 0, 8]], 1),
	(0, [[9, 3, 0], [1, 1, 6]], 1),
	(8, [[6, 2, 1, 8], [1, 4, 4, 5]], 1),
	(8, [[0, 8, 0], [4, 2, 5]], 1),
	(9, [[9, 4, 9, 8, 8]], 2)
]

@pytest.mark.parametrize("numero, matriz, output", test_cases)

def test_conta_numero(numero, matriz, output, solution):
    imp = importlib.import_module(solution)
    assert imp.conta_numero(numero, matriz) == output

