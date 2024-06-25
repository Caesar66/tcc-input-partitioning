import pytest
import importlib

test_cases = [
    ((0,0,1,1), (0,0,1,1), True),
    ((0,0,1,1), (-3,-3,-2,-2), False),
    ((-3,-3,2,2), (-1,-1,0,0), True),
    ((-2,-2,-1,-1), (-2,-2,-1,-1), True),
    ((-3,-3,-2,-2), (-1,-1,1,1), False),
    ((-1,-1,1,1), (2,2,3,3), False),
    ((-2,-2,3,3), (-4,-4,-3,-3), False),
    ((-2,-2,-1,-1), (2,2,4,4), False),
    ((2,2,3,3), (-2,-2,4,4),True)
]

@pytest.mark.parametrize("tupla1, tupla2, output", test_cases)

def test_colisao(tupla1, tupla2, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colisao(tupla1, tupla2) == output
