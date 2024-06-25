import pytest
import importlib

test_cases = [
    (0, 0),
    (1, 1),
    (2, 1.5),
    (23, 3.73),
    (22, 3.69)
]

@pytest.mark.parametrize("n, output", test_cases)
def test_soma_h(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.soma_h(n) == output
