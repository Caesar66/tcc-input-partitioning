import pytest
import importlib

test_cases = [
	('111aaa', '222bbb', '111aaa222bbb222bbb111aaa'),
    ('', '', ''),
    ('cha', '222', 'cha222222cha'),
    ('1000', 'mil', '1000milmil1000'),
    ('100', '19', '1001919100'),
    ('GUARDA ', 'chuva', 'GUARDA chuvachuvaGUARDA '),
    ('8000 space', '', '8000 space8000 space'),
    ('', '9s', '9s9s')
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_concatenacao(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.concatenacao(a, b) == output
