import pytest
import importlib

test_cases = [
    ([], 1, []),
    ([], -1.0, []),
    ([1, 2, 3], 1, [1, 2, 3]),
    ([-3.0, -3.1, -3.2], -2.0, []),
    ([-7.2, -2, -2], -2, [-2, -2]),
    ([5, 3.9, 11.1, 1], 2.2, []),
    ([-2, -4, -5], 2, [-2, -4]),
    ([4.4, -3.1, -6.8], -2.2, [4.4])
]

@pytest.mark.parametrize("lista_numero, n, output", test_cases)

def test_filtraMultiplos(lista_numero, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtraMultiplos(lista_numero, n) == output
