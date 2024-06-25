import pytest
import importlib

test_cases = [
    ([], True),
    ([[1]], True),
    ([[1],[4],[9],[6],[-6],[-5]], False),
    ([[1,100,1000,10000],[0,0,0,0],[-100,2,2,1]], False)
]

@pytest.mark.parametrize("matriz, output", test_cases)

def test_eh_quadrada(matriz, output, solution):
	imp = importlib.import_module(solution)
	assert imp.eh_quadrada(matriz) == output

