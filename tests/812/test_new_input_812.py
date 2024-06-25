import pytest
import importlib

test_cases = [
    ('', ''),
    ('FOGO...!?.', 'FOGO      '),
    ('presta atenção, vou falar última vez: dois guarda-chuvas; um rolo de papel higienico; uma caneta', 'presta atenção  vou falar última vez  dois guarda chuvas  um rolo de papel higienico  uma caneta')
]

@pytest.mark.parametrize("str, output", test_cases)

def test_retira_pontuacao(str, output, solution):
	imp = importlib.import_module(solution)
	assert imp.retira_pontuacao(str) == output
