import pytest
import importlib

test_cases = [
	(4, 24),
	(9, 362880),
	(5, 120),
	(2, 2),
	(7, 5040),
	(1, 1),
	(6, 720),
	(8, 40320),
	(3, 6)
]

@pytest.mark.parametrize("numero, output", test_cases)
def test_fatorial(numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.fatorial(numero) == output
