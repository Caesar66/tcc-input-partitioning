import pytest
import importlib

test_cases = [
    ([100, 100, 100], 80, 50, False),
    ([100, 100, 100], 100, 50, False),
    ([100, 100, 100], 80, 100, False),
    ([90, 90, 90], 100, 100, True),
    ([90, 90, 100], 100, 90, True),
    ([90, 90, 100], 90, 100, True),
    ([90, 90, 100], 90, 90, True),
    ([80, 90, 100], 90, 80, True),
    ([80, 90, 100], 80, 90, True)
]

@pytest.mark.parametrize("lst, h, w, output", test_cases)
def test_colchao(lst, h, w, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colchao(lst, h, w) == output
