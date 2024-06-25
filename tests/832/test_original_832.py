import pytest
import importlib

test_cases = [
	([], True),
	([[4, 5, 0, 1, 6], [7, 4, 3, 3, 4]], False),
	([[9], [6], [1], [1]], False),
	([[8, 8, 5, 6], [3, 3, 6, 3], [8, 2, 8, 6], [2, 7, 8, 2], [4, 4, 2, 9]], False),
	([[3, 9, 0, 4, 3], [6, 8, 3, 1, 5], [9, 2, 4, 1, 9]], False),
	([[1, 2], [8, 8], [4, 7], [1, 0], [5, 3]], False),
	([[1, 2, 7], [6, 4, 7], [2, 7, 2], [7, 0, 8]], False),
	([[2, 1, 8, 3, 8]], False),
	([[6, 3], [9, 2], [4, 0], [8, 0], [4, 8]], False),
	([[1, 3, 8, 7, 1], [8, 3, 0, 2, 5]], False),
	([[1, 1, 2, 4], [2, 7, 6, 2], [5, 9, 8, 1], [5, 9, 5, 7], [5, 2, 6, 2]], False),
	([[0, 5, 2, 2, 2], [0, 5, 2, 2, 6], [0, 5, 5, 7, 1]], False),
	([[1, 7]], False),
	([[3], [4], [3], [3], [8]], False),
	([[9, 6], [0, 2], [5, 8], [8, 2]], False),
	([[6, 1, 9]], False),
	([[8, 0], [3, 8], [7, 2], [0, 8]], False),
	([[1, 1, 8, 9, 9], [1, 0, 1, 2, 6], [9, 2, 6, 1, 1], [1, 9, 7, 9, 8], [6, 0, 2, 6, 7]], True),
	([[2, 3], [5, 9], [9, 5], [3, 5], [1, 2]], False),
	([[7, 3], [5, 1], [7, 9], [0, 7]], False),
	([[8, 6, 8]], False)
]

@pytest.mark.parametrize("matriz, output", test_cases)

def test_eh_quadrada(matriz, output, solution):
	imp = importlib.import_module(solution)
	assert imp.eh_quadrada(matriz) == output

