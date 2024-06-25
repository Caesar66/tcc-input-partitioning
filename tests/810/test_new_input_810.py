import pytest
import importlib

test_cases = [
    ('', ''),
    ('FOGO...!?.', 'fogo'),
    ('presta atenção, vou falar última vez: dois guarda-chuvas; um rolo de papel higienico; uma caneta', 'caneta uma higienico papel de rolo um chuvas guarda dois vez última falar vou atenção presta')
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_inverte(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.inverte(frase) == output

