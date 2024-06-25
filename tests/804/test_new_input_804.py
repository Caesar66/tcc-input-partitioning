import pytest
import importlib

test_cases = [
    ((-1, -1, 3, 1), ()),
    ((1, 2, -3, -4), (2, -4)),
    ((-2, -2, 2, 2), (-2, -2, 2, 2)),
    ((-2, -2, -2, -2), (-2, -2, -2, -2)),
    ((-1, -1, -5, -5), ()),
    ((-1, -2, -5, -5), (-2,)),
    ((2, 2, 2, 2), (2, 2, 2, 2)),
    ((0, 1, 2, 1), (0, 2)),
    ((3, 3, 3, 3), ())
]

@pytest.mark.parametrize("tupla, output", test_cases)

def test_filtra_pares(tupla, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtra_pares(tupla) == output
