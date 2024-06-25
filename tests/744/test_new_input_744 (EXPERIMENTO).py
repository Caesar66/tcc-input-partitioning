import pytest
import importlib

test_cases = [
    ('', '###'),
	('A', '##A#'),
	('1', '##1#'),
	('&', '##&#'),
	('A1', '#A#1#'),
	('A&', '#A#&#'),
	('1&', '#1#&#'),
	('Aab198 &!', '#Aab1#98 &!#')
]

@pytest.mark.parametrize("s, output", test_cases)

def test_hashtag(s, output, solution):
	imp = importlib.import_module(solution)
	assert imp.hashtag(s) == output
