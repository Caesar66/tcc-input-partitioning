import pytest
import importlib

test_cases = [
	('Ficou muito tempo com a cara virada para ele.', 'Ficou muito tempo com a cara virada para ele '),
	('Tio Cosme ensinou-lhe gamão.', 'Tio Cosme ensinou lhe gamão '),
	('Oh!', 'Oh '),
	('conte-me as festas da Coroação!', 'conte me as festas da Coroação '),
	('As curiosidades de Capitu dão para um capítulo.', 'As curiosidades de Capitu dão para um capítulo '),
	('Júlio César!', 'Júlio César '),
	('E quanto valia cada sestércio?', 'E quanto valia cada sestércio '),
	('Quando é que botou estas?', 'Quando é que botou estas '),
	('São jóias viúvas, como eu, Capitu.', 'São jóias viúvas  como eu  Capitu '),
	('Anda apanhar um capotinho, Capitu, dizia-lhe ele.', 'Anda apanhar um capotinho  Capitu  dizia lhe ele ')
]

@pytest.mark.parametrize("str, output", test_cases)

def test_retira_pontuacao(str, output, solution):
	imp = importlib.import_module(solution)
	assert imp.retira_pontuacao(str) == output
