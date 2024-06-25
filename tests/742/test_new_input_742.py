import pytest
import importlib

test_cases = [
    ('S','B',0, 'B'),
    ('Prato cheio!','a',4, 'Prata cheio!'),
    ('farinha','c',0, 'carinha'),
    ('a agua ta seca','o',0, 'o agua ta seca'),
    ('metallica','a',1, 'matallica'),
]

@pytest.mark.parametrize("s, x, i, output", test_cases)

def test_substitui(s, x, i, output, solution):
	imp = importlib.import_module(solution)
	assert imp.substitui(s, x, i) == output
