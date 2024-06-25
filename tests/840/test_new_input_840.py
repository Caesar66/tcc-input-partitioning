import pytest
import importlib

test_cases = [
    (1,1,1, 0),
    (2,3,5, 1),
    (4,6,10, 2),
    (1,3,6, 0),
    (1,4,5, 0),
    (2,2,6, 0),
    (2,4,4, 0),
    (3,2,5, 0),
    (3,3,4, 0)
]

@pytest.mark.parametrize("a, b, c, output", test_cases)

def test_bolos(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.bolos(a, b, c) == output
