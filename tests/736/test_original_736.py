import pytest
import importlib

test_cases = [
	('arborista', 'sigilar', 'arboristasigilarsigilararborista'),
	('sustivéreis', 'caleira', 'sustivéreiscaleiracaleirasustivéreis'),
	('somatotropas', 'repelir', 'somatotropasrepelirrepelirsomatotropas'),
	('lamentar', 'Lérida', 'lamentarLéridaLéridalamentar'),
	('', 'segue', 'seguesegue'),
	(' ', 'musicologia', ' musicologiamusicologia '),
	('crápula', 'generante', 'crápulagenerantegenerantecrápula'),
	('persecução', 'esticanço', 'persecuçãoesticançoesticançopersecução'),
	('caleira', 'fanático', 'caleirafanáticofanáticocaleira'),
	('cólico', 'linguístico', 'cólicolinguísticolinguísticocólico'),
	('cobiçoso', 'penúltimo', 'cobiçosopenúltimopenúltimocobiçoso'),
	('multimédia', 'subtractivo', 'multimédiasubtractivosubtractivomultimédia'),
	('nevoeirada', 'predilecção', 'nevoeiradapredilecçãopredilecçãonevoeirada'),
	('panelada', ' ', 'panelada  panelada'),
	('Lérida', 'convêm', 'LéridaconvêmconvêmLérida'),
	('trajo', 'espaldar', 'trajoespaldarespaldartrajo'),
	('carcereiro', 'europeízem', 'carcereiroeuropeízemeuropeízemcarcereiro'),
	('alcatraz', 'gauchai', 'alcatrazgauchaigauchaialcatraz'),
	('boateiro', 'anticolérico', 'boateiroanticoléricoanticoléricoboateiro'),
	('duodecénio', 'somatotropas', 'duodecéniosomatotropassomatotropasduodecénio'),
	('cirzo', 'Mark', 'cirzoMarkMarkcirzo'),
	('pintalgar', '', 'pintalgarpintalgar')
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_concatenacao(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.concatenacao(a, b) == output
