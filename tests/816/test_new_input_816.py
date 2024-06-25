import pytest
import importlib

test_cases = [
    ([],0, []),
    ([],-1, []),
    ([0],-1, [0]),
    ([-2],0, []),
    ([0, -2], -2, [0]),
    ([0, 1], 0, [1]),
    ([-2, -1], -2, [-1])
]

@pytest.mark.parametrize("lista, n, output", test_cases)
def test_maiores(lista, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.maiores(lista, n) == output
