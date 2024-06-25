import pytest
import importlib

test_cases = [
	('e quanto valia cada sestércio?', 's', 3, -1),
	('tio cosme ensinou-lhe gamão', 's', 1, 6),
	('nascera muito depois daquelas festas célebres', 'e', 1, 4),
	('que fazia tudo', 'e', 1, 2),
	('tu quoque brute?', 't', 1, 0),
	('as curiosidades de capitu dão para um capítulo', 'p', 4, -1),
	('ficou muito tempo com a cara virada para ele', 'f', 1, 0),
	('conte-me as festas da coroação', 'e', 1, 4),
	('foi pelas festas da coroação', 's', 4, -1)
]

@pytest.mark.parametrize("frase, letra, ocorrencia, output", test_cases)

def test_posLetra(frase, letra, ocorrencia, output, solution):
	imp = importlib.import_module(solution)
	assert imp.posLetra(frase, letra, ocorrencia) == output
