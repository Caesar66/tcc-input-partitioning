import pytest
import importlib

test_cases = [	
    (5, [], 1),
	(0, [], 0),
	(11, [6], 2),
	(14, [4], 4),
	(16, [6], 3),
	(1, [3], 1),
	(3, [1], 3),
	(16, [], 4),
	(1, [], 1),
	(12, [], 3)
]

@pytest.mark.parametrize("passageiros, capacidade, output", test_cases)

def test_carros(passageiros, capacidade, output, solution):
	imp = importlib.import_module(solution)
	assert imp.carros(passageiros, *capacidade) == output
