import pytest
import importlib

test_cases = [
    ('','',1, -1),
    ('barba','s',1, -1),
    ('cachorro','h',1, 3),
    ('paralelepípedo','p',2, 8),
    ('tem dois reais aqui','i',3, 18),
    ('cachorro','h',2, -1),
    ('Fala baixo aí!','v',1, -1),
    ('ela ta com raiva','a',1, 2),
    ('violoncelo','o',4, -1)
]

@pytest.mark.parametrize("frase, letra, ocorrencia, output", test_cases)

def test_posLetra(frase, letra, ocorrencia, output, solution):
	imp = importlib.import_module(solution)
	assert imp.posLetra(frase, letra, ocorrencia) == output
