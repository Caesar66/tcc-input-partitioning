import pytest
import importlib

test_cases = [
	((207, 369, -5, 812), (812,)),
	((945, 74, 205, 654), (74, 654)),
	((991, 775, 5, 394), (394,)),
	((-40, 698, 538, 408), (-40, 698, 538, 408)),
	((37, 705, 599, 636), (636,)),
	((878, -47, 465, 319), (878,)),
	((628, 885, 14, 34), (628, 14, 34)),
	((929, 215, 308, 903), (308,)),
	((575, 641, 851, 707), ()),
	((146, 563, 249, 270), (146, 270)),
	((916, 123, 417, 627), (916,)),
	((147, 613, 609, 267), ())
]

@pytest.mark.parametrize("tupla, output", test_cases)

def test_filtra_pares(tupla, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtra_pares(tupla) == output
