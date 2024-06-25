import pytest
import importlib


ct1 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
]

ct2 = [
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25.6, 26, 27, 28, 29, 30],
    [31, 32, 33.9, 34, 35, 36, 37, 38, 39, 40.6],
    [10, 9, 3, 5, 1.2, 2, 4, 6, 7, 8],
    [41, 42, 43, 44.1, 45, 46, 47, 48, 49.2, 50.6],
    [51, 52, 53.0, 54, 55, 56, 57, 58, 59, 60]
]

ct3 = [
    [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.2, 18.0, 19.0, 20.0],
    [21.0, 22.4, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0],
    [31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0],
    [41.0, 42.0, 43.9, 44.0, 45.0, 46.0, 47.3, 48.0, 49.0, 50.0],
    [51.0, 52.0, 53.1, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0],
    [6.0, 7.0, 8.0, 9.0, 10.0, 2.0, 3.0, 4.0, 5.0, 1.0]
]


test_cases = [
    (ct1, (1, 1, 1)),
    (ct2, (4, 1.2, 5)),
    (ct3, (6, 1.0, 10)),
]

@pytest.mark.parametrize("matriz, output", test_cases)

def test_melhor_volta(matriz, output, solution):
    imp = importlib.import_module(solution)
    assert imp.melhor_volta(matriz) == output

