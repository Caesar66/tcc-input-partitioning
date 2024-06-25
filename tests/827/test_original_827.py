import pytest
import importlib

test_cases = [
	(26, 4),
	(-9, 0),
	(-4, 0),
	(-18, 0),
	(77, 4),
	(63, 6),
	(45, 6),
	(16, 5),
	(57, 4),
	(0, 0)
]

@pytest.mark.parametrize("n, output", test_cases)

def test_qtd_divisores(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.qtd_divisores(n) == output
