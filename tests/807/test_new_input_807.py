import pytest
import importlib

test_cases = [
    ('Eu.', 1),
    ('Eu!', 1),
    ('Eu?', 1),
    ('Eu...', 1),
    ('Eu. Tu! Nós? Eles...', 4),
    ('Eu. Tu!', 2),
    ('Nós? Eles...', 2),
    ('', 0),
    ('....!?', 4)
]

@pytest.mark.parametrize("a, output", test_cases)

def test_conta_frases(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.conta_frases(a) == output
