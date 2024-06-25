import pytest
import importlib

# Input:
# [['Cormengo', 'Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 2]]]

# Output:
# {'Cormengo': 4, 'Flamínthians': 1}

test_cases = [
	([['Botagama', 'Cornense', [4, 1]], ['Cornense', 'Botagama', [1, 5]]], {'Botagama': 6, 'Cornense': 0}),
	([['Flamínthians', 'São Fogo', [5, 4]], ['São Fogo', 'Flamínthians', [4, 3]]], {'Flamínthians': 3, 'São Fogo': 3}),
	([['Vascofogo', 'Santasco', [5, 0]], ['Santasco', 'Vascofogo', [1, 3]]], {'Vascofogo': 6, 'Santasco': 0}),
	([['Vasínthians', 'Santeiras', [0, 0]], ['Santeiras', 'Vasínthians', [5, 3]]], {'Vasínthians': 1, 'Santeiras': 4}),
	([['Botameiras', 'São Fogo', [1, 2]], ['São Fogo', 'Botameiras', [2, 2]]], {'Botameiras': 1, 'São Fogo': 4}),
	([['Cormengo', 'Cornense', [3, 3]], ['Cornense', 'Cormengo', [4, 4]]], {'Cormengo': 2, 'Cornense': 2}),
	([['Santasco', 'Flumipaulo', [3, 5]], ['Flumipaulo', 'Santasco', [1, 5]]], {'Santasco': 3, 'Flumipaulo': 3}),
	([['Santeiras', 'Fluminantos', [1, 4]], ['Fluminantos', 'Santeiras', [2, 0]]], {'Santeiras': 0, 'Fluminantos': 6}),
	([['São Vasco', 'São Fogo', [2, 5]], ['São Fogo', 'São Vasco', [4, 5]]], {'São Vasco': 3, 'São Fogo': 3}),
	([['Corgama', 'Vasínthians', [4, 5]], ['Vasínthians', 'Corgama', [2, 1]]], {'Corgama': 0, 'Vasínthians': 6}),
	([['Santeiras', 'São Fogo', [1, 3]], ['São Fogo', 'Santeiras', [4, 3]]], {'Santeiras': 0, 'São Fogo': 6}),
	([['Santasco', 'Flameiras', [3, 0]], ['Flameiras', 'Santasco', [3, 0]]], {'Santasco': 3, 'Flameiras': 3}),
	([['Santasco', 'Fluminantos', [3, 4]], ['Fluminantos', 'Santasco', [1, 0]]], {'Santasco': 0, 'Fluminantos': 6}),
	([['Botameiras', 'Cornense', [2, 4]], ['Cornense', 'Botameiras', [3, 2]]], {'Botameiras': 0, 'Cornense': 6}),
	([['Botameiras', 'Paulo da Gama', [4, 0]], ['Paulo da Gama', 'Botameiras', [2, 5]]], {'Botameiras': 6, 'Paulo da Gama': 0})
]

@pytest.mark.parametrize("lista, output", test_cases)

def test_pontos_por_time(lista, output, solution):
	imp = importlib.import_module(solution)
	assert imp.pontos_por_time(lista) == output
