import pytest
import importlib

test_cases = [
	(1.0, 0.5, 2.0),
	(0, 0.1, 0.0),
	(52.33, 3.89, 13.0),
	(27.72, 4.2, 6.0),
	(8.61, 0.7, 12.0),
	(53.28, 1.47, 36.0),
	(88.18, 1.36, 64.0),
	(72.35, 9.93, 7.0),
	(79.96, 1.43, 55.0),
	(48.24, 5.35, 9.0)
]

@pytest.mark.parametrize("dinheiro, preco, output", test_cases)

def test_num_bombons(dinheiro, preco, output, solution):
	imp = importlib.import_module(solution)
	assert imp.num_bombons(dinheiro, preco) == output
