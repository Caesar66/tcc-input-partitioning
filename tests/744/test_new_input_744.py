import pytest
import importlib

test_cases = [
    ('', '###'),
    ('A', '##A#'),
    ('A1', '#A#1#'),
    ('A1&', '#A#1&#')
]

@pytest.mark.parametrize("s, output", test_cases)

def test_hashtag(s, output, solution):
	imp = importlib.import_module(solution)
	assert imp.hashtag(s) == output
