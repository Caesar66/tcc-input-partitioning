import pytest
import importlib

test_cases = [
    (0, 1, 0),
    (0, 1.5, 0),
    (12.5, 2.5, 5),
    (3, 3, 1),
    (2.5, 3, 0),
    (10, 2, 5),
    (1.5, 1.5, 1)
]

@pytest.mark.parametrize("dinheiro, preco, output", test_cases)

def test_num_bombons(dinheiro, preco, output, solution):
	imp = importlib.import_module(solution)
	assert imp.num_bombons(dinheiro, preco) == output
