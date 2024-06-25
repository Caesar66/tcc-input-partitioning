import pytest
import importlib

test_cases = [
    (0, [4], 0),
    (0, [], 0),
    (5, [], 1),
    (6, [6], 1),
    (6, [], 2),
    (5, [3], 2),
    (1, [], 1)
]

@pytest.mark.parametrize("passageiros, capacidade, output", test_cases)

def test_carros(passageiros, capacidade, output, solution):
	imp = importlib.import_module(solution)
	assert imp.carros(passageiros, *capacidade) == output
