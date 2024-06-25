import pytest
import importlib

test_cases = [
	(20, 15, 10, 2),
	(20, 15, 500, 5),
	(2, 6, 50, 1),
	(6, 9, 15, 3),
	(2, 3, 5, 1),
	(2, 50, 3, 0),
	(10, 1, 5, 0),
	(0, 5, 5, 0),
	(4, 6, 9, 1),
	(4, 6, 10, 2)
]

@pytest.mark.parametrize("a, b, c, output", test_cases)

def test_bolos(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.bolos(a, b, c) == output
