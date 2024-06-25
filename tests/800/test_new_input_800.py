import pytest
import importlib

test_cases = [
    ([],{}, 0),
    (['biscoito', 'queijo'],{'biscoito':1.00, 'manteiga':2.00}, 1.00),
    ([],{'biscoito':1.00}, 0),
    (['biscoito', 'biscoito'],{}, 0),
    (['manteiga'],{'manteiga':1.00}, 1.00),
    (['manteiga', 'manteiga', 'biscoito'],{'manteiga':1.00}, 2.00),
    (['manteiga', 'manteiga'],{'manteiga':1.00, 'queijo':2.50}, 2.00)
]

@pytest.mark.parametrize("compras, produto, output", test_cases)
def test_total(compras, produto, output, solution):
	imp = importlib.import_module(solution)
	assert imp.total(compras, produto) == output
