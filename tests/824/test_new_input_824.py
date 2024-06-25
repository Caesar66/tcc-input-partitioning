import pytest
import importlib

test_cases = [
    ('', ''),
    ('PEI!','PEI!'),
    ('ora! PEÇA 1 enTAO', 'oRa! PEÇA 1 eNTAO'),
    ('agora? qualquer', 'aGoRa? QuaLQueR')
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_uppCons(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.uppCons(frase) == output
