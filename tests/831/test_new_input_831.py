import pytest
import importlib

test_cases = [
    ('Cachorro', 'capachoporropo'),
    ('uau uau', 'upuapaupu upuapaupu'),
    (' ', ' '),
    ('zzz', 'zzz'),
    ('e daí', 'epe dapaípí'),
    ('oião', 'opoipiãpãopo')
]

@pytest.mark.parametrize("palavra, output", test_cases)

def test_lingua_p(palavra, output, solution):
	imp = importlib.import_module(solution)
	assert imp.lingua_p(palavra) == output
