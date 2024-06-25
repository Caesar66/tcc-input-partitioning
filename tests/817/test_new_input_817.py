import pytest
import importlib

test_cases = [
    ([1], []),
    ([-1], []),
    ([2, -1, -1, -2], [2]),
    ([2, 2, 3, 3], [3, 3]),
    ([-2, -3, -4, -3, -9], [-4, -3, -3, -2]),
    ([3, 7, 4, 0, 1, 2], [3, 4, 7])
]

@pytest.mark.parametrize("notas_alunos, output", test_cases)

def test_acima_da_media(notas_alunos, output, solution):
	imp = importlib.import_module(solution)
	assert imp.acima_da_media(notas_alunos) == output
