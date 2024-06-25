import pytest
import importlib

test_cases = [
    ('cachorro', 1),
    (' gatinho', 1),
    ('macio ', 1),
    (' 15mil ', 1),
    ('', 0),
    ('    ', 0),
    ('para quedas', 2),
    (' valeu amigo ', 2),
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_quant_palavras(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.quant_palavras(frase) == output
