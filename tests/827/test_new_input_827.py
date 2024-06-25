import pytest
import importlib

test_cases = [
    (2, 2),
    (3, 2),
    (4, 3),
    (9, 3),
    (-2, 0),
    (-9, 0)
]

@pytest.mark.parametrize("n, output", test_cases)

def test_qtd_divisores(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.qtd_divisores(n) == output
