import pytest
import importlib

test_cases = [
	('tempo', {'tempo':1}),
    ('', {}),
    ('din din', {'din':2}),
    ('tinha tinha dito', {'tinha':2, 'dito':1}),
    ('gente brava', {'gente':1, 'brava':1}),
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_freq_palavras(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.freq_palavras(frase) == output
