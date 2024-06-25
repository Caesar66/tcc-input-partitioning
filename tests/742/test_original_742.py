import pytest
import importlib

test_cases = [
	('delínquo', 'o', 2, 'deoínquo'),
	('destingir', 'o', 8, 'destingio'),
	('OGMA', 'z', 2, 'OGzA'),
	('centro', 'i', 1, 'cintro'),
	('dragagem', 'o', 5, 'dragaoem'),
	(' ', 'x', 0, 'x'),
	('Schiller', 'k', 0, 'kchiller'),
	('isotónico', 'a', 2, 'isatónico'),
	('predilecção', 'n', 9, 'predilecçno'),
	('séquito', 's', 5, 'séquiso'),
	('crápula', 'g', 2, 'crgpula'),
	('barão', 'q', 2, 'baqão'),
	('candelabro', 'b', 4, 'candblabro'),
	('virginalizar', 'g', 4, 'virggnalizar'),
	('cobiçoso', 's', 2, 'cosiçoso'),
	('atomismo', 'o', 7, 'atomismo'),
	('esticanço', 'y', 6, 'esticayço'),
	('festinhas', 'i', 3, 'fesiinhas'),
	('panelada', 'd', 4, 'panedada'),
	('famigerado', 'p', 4, 'famiperado'),
	('subtractivo', 'd', 2, 'sudtractivo'),
	('musicologia', 'k', 4, 'musikologia'),
	('sorrir', 'o', 1, 'sorrir'),
	('ogivado', 's', 3, 'ogisado'),
	('europeízem', 'q', 5, 'europqízem'),
	('carcereiro', 'g', 4, 'carcgreiro'),
	('troçar', 'f', 3, 'trofar'),
	('aborto', 'o', 0, 'oborto'),
	('Lérida', 'f', 4, 'Lérifa'),
	('espaldar', 'x', 1, 'expaldar'),
	('linguístico', 't', 0, 'tinguístico'),
	('cagaçal', 'i', 1, 'cigaçal'),
	('sagaz', 'b', 1, 'sbgaz'),
	('traziam', 'e', 3, 'traeiam'),
	('advirdes', 'b', 6, 'advirdbs'),
	('exultar', 'u', 0, 'uxultar'),
	('sustivéreis', 'h', 4, 'susthvéreis'),
	('Mark', 'l', 2, 'Malk'),
	('Mussolini', 'h', 3, 'Musholini'),
	('previne', 'h', 2, 'prhvine'),
	('delirar', 'f', 1, 'dflirar'),
	('nevoeirada', 'l', 6, 'nevoeilada'),
	('cirzo', 's', 2, 'ciszo'),
	('caleira', 's', 0, 'saleira'),
	('generante', 'l', 0, 'lenerante'),
	('regresso', 'm', 6, 'regresmo'),
	('matutar', 'u', 6, 'matutau'),
	('sigilar', 'w', 6, 'sigilaw'),
	('particularista', 'l', 2, 'palticularista'),
	('borbulhento', 'r', 6, 'borbulrento'),
	('divindade', 'i', 8, 'divindadi'),
	('confessor', 'x', 4, 'confxssor'),
	('luso', 'k', 2, 'luko'),
	('lixoso', 'x', 4, 'lixoxo'),
	('inclusão', 'p', 6, 'incluspo'),
	('cacheiro', 'u', 1, 'cucheiro'),
	('multimédia', 'i', 2, 'muitimédia'),
	('paludismo', 'c', 7, 'paludisco'),
	('segue', 'q', 3, 'segqe'),
	('vivificativo', 'c', 0, 'civificativo'),
	('cólico', 't', 5, 'cólict'),
	('terreno', 'z', 6, 'terrenz'),
	('higienizar', 'j', 4, 'higijnizar'),
	('imperturbado', 'w', 1, 'iwperturbado'),
	('lamentar', 'g', 3, 'lamgntar'),
	('Kennedy', 'g', 2, 'Kegnedy'),
	('adviéreis', 'l', 1, 'alviéreis'),
	('penúltimo', 'w', 4, 'penúwtimo'),
	('duodecénio', 't', 2, 'dutdecénio'),
	('drogaria', 'f', 5, 'drogafia'),
	('arpear', 'o', 2, 'aroear'),
	('sustiveram', 'o', 0, 'oustiveram'),
	('persecução', 'w', 9, 'persecuçãw'),
	('intercelular', 'c', 11, 'intercelulac'),
	('ressentir', 'p', 4, 'resspntir'),
	('trajo', 'f', 4, 'trajf'),
	('filonianos', 'b', 9, 'filonianob'),
	('boateiro', 'g', 6, 'boateigo'),
	('arborista', 'p', 1, 'apborista'),
	('escorrer', 'i', 7, 'escorrei'),
	('amoladura', 'u', 4, 'amoludura'),
	('entretendo', 'k', 7, 'entretekdo'),
	('equitativo', 'i', 7, 'equitativo'),
	('cabular', 'c', 3, 'cabclar'),
	('voraz', 'k', 3, 'vorkz'),
	('humildade', 'y', 5, 'humilyade'),
	('dúbio', 't', 2, 'dútio'),
	('alcatraz', 'l', 7, 'alcatral'),
	('gauchai', 'v', 3, 'gauvhai'),
	('convêm', 'v', 3, 'convêm'),
	('somatotropas', 'l', 6, 'somatolropas'),
	('vagão', 'e', 3, 'vageo'),
	('fanático', 'x', 7, 'fanáticx'),
	('saberdes', 'e', 5, 'saberees'),
	('bit', 'j', 0, 'jit'),
	('intravável', 'x', 5, 'intraxável'),
	('repelir', 't', 1, 'rtpelir'),
	('anticolérico', 'j', 11, 'anticoléricj'),
	('crestar', 'l', 4, 'creslar'),
	('pintalgar', 'x', 2, 'pixtalgar')
]

@pytest.mark.parametrize("s, x, i, output", test_cases)

def test_substitui(s, x, i, output, solution):
	imp = importlib.import_module(solution)
	assert imp.substitui(s, x, i) == output