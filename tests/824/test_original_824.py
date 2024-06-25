import pytest
import importlib

test_cases = [
	('Tio Cosme ensinou-lhe gamão.', 'Tio CoSMe eNSiNou-LHe GaMão.'),
	('Júlio César!', 'JúLio CéSaR!'),
	('Anda apanhar um capotinho, Capitu, dizia-lhe ele.', 'ANDa aPaNHaR uM CaPoTiNHo, CaPiTu, DiZia-LHe eLe.'),
	('Fui devagar, mas ou o pé ou o espelho traiu-me.', 'Fui DeVaGaR, MaS ou o Pé ou o eSPeLHo TRaiu-Me.'),
	('conte-me as festas da Coroação!', 'CoNTe-Me aS FeSTaS Da CoRoaÇão!'),
	('Oh!', 'OH!'),
	('As curiosidades de Capitu dão para um capítulo.', 'AS CuRioSiDaDeS De CaPiTu Dão PaRa uM CaPíTuLo.'),
	('Ficou muito tempo com a cara virada para ele.', 'FiCou MuiTo TeMPo CoM a CaRa ViRaDa PaRa eLe.'),
	('São jóias viúvas, como eu, Capitu.', 'São JóiaS ViúVaS, CoMo eu, CaPiTu.'),
	('Um homem que podia tudo!', 'UM HoMeM Que PoDia TuDo!')
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_uppCons(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.uppCons(frase) == output
