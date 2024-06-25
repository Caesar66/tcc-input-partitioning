import pytest
import importlib

test_cases = [
	(174, False),
	(5041, False),
	(4, False),
	(169, False),
	(216, False),
	(235, False),
	(37, True),
	(11, True),
	(33, False),
	(239, True),
	(241, True),
	(281, True),
	(112, False),
	(51, False),
	(263, True),
	(289, False),
	(121, False),
	(286, False),
	(288, False),
	(228, False)
]

@pytest.mark.parametrize("n, output", test_cases)

def test_primo(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.primo(n) == output
