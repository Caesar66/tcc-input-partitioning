import pytest
import importlib

test_cases = [
	(6, 2.45),
	(28, 3.93),
	(6, 2.45),
	(27, 3.89),
	(10, 2.93),
	(16, 3.38),
	(20, 3.6),
	(1, 1.0),
	(5, 2.28),
	(10, 2.93)
]

@pytest.mark.parametrize("n, output", test_cases)
def test_soma_h(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.soma_h(n) == output
