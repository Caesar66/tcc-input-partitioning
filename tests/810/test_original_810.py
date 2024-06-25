import pytest
import importlib

test_cases = [
	('Tio Cosme ensinou-lhe gamão.', 'gamão lhe ensinou cosme tio'),
	('Foi pelas festas da Coroação.', 'coroação da festas pelas foi'),
	('Ficou muito tempo com a cara virada para ele.', 'ele para virada cara a com tempo muito ficou'),
	('Nascera muito depois daquelas festas célebres.', 'célebres festas daquelas depois muito nascera'),
	('As curiosidades de Capitu dão para um capítulo.', 'capítulo um para dão capitu de curiosidades as'),
	('que fazia tudo!', 'tudo fazia que'),
	('São jóias viúvas, como eu, Capitu.', 'capitu eu como viúvas jóias são'),
	('Fui devagar, mas ou o pé ou o espelho traiu-me.', 'me traiu espelho o ou pé o ou mas devagar fui'),
	('E quanto valia cada sestércio?', 'sestércio cada valia quanto e'),
	('Anda apanhar um capotinho, Capitu, dizia-lhe ele.', 'ele lhe dizia capitu capotinho um apanhar anda')
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_inverte(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.inverte(frase) == output
