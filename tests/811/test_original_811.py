import pytest
import importlib

test_cases = [
	([36, 190, 209], 187, 248, True),
	([24, 192, 207], 193, 246, True),
	([30, 197, 202], 182, 165, False),
	([22, 180, 204], 181, 126, True),
	([28, 187, 215], 183, 144, False),
	([34, 182, 205], 182, 142, True),
	([38, 195, 211], 191, 139, False),
	([21, 199, 202], 199, 201, True),
	([23, 194, 205], 184, 164, False),
	([24, 187, 207], 194, 99, True)
]

@pytest.mark.parametrize("lst, h, w, output", test_cases)
def test_colchao(lst, h, w, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colchao(lst, h, w) == output
