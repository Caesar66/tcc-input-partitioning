import pytest
import importlib

test_cases = [
	([9, 0, 7, 8], [7, 8, 9]),
	([6, 2], [6]),
	([5, 3, 2, 0, 8, 1, 7, 6], [5, 6, 7, 8]),
	([8, 1], [8]),
	([6, 2, 0, 4, 9, 8, 5, 7], [6, 7, 8, 9]),
	([8, 0, 1, 5], [5, 8]),
	([6], []),
	([1, 9, 0, 3], [9]),
	([1, 5, 8, 3, 0], [5, 8]),
	([8, 9, 1, 7, 0, 5, 3, 2, 4, 6], [5, 6, 7, 8, 9])
]

@pytest.mark.parametrize("notas_alunos, output", test_cases)

def test_acima_da_media(notas_alunos, output, solution):
	imp = importlib.import_module(solution)
	assert imp.acima_da_media(notas_alunos) == output
