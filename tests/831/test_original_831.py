import pytest
import importlib

test_cases = [
	('carcereiro', 'caparceperepeipiropo'),
	('festinhas', 'fepestipinhapas'),
	('penúltimo', 'pepenúpúltipimopo'),
	('intravável', 'ipintrapavápávepel'),
	('sustivéreis', 'supustipivépérepeipis'),
	('higienizar', 'hipigipiepenipizapar'),
	('ogivado', 'opogipivapadopo'),
	('borbulhento', 'boporbupulhepentopo'),
	('candelabro', 'capandepelapabropo'),
	('advirdes', 'apadvipirdepes')
]

@pytest.mark.parametrize("palavra, output", test_cases)

def test_lingua_p(palavra, output, solution):
	imp = importlib.import_module(solution)
	assert imp.lingua_p(palavra) == output
