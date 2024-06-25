import pytest
import importlib

test_cases = [
    (0, False),
    (1, False),
    (2, True),
    (115523, True),
    (24000002, False)
]

@pytest.mark.parametrize("n, output", test_cases)

def test_primo(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.primo(n) == output
