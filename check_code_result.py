from copy import deepcopy
import errno
import os
import signal
import functools
import time


class timeout:
    def __init__(self, seconds=1):
        self.seconds = seconds
    def handle_timeout(self, signum, frame):
        raise TimeoutError()
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)


def main(test):
	test = test[:-1]
	
	def uppCons(frase):
		"""funcao que recebe uma frase e retorna a mesma só que com todas as consoantes em maiúsculas
		str -> str"""
		
		maius = 'bcçdfghjklmnpqrstvwyz'
		i = 0
		
		while len(frase) > i:
		    if frase[i] in maius:
		        frase = frase.replace(frase[i], frase[i].upper())
		    i = i + 1 
		
		return frase
    
		
	return uppCons	(*test)


test_cases = [

	("aeiou", "aeiou"),
	("bcdfgh", "BCDFGH"),
	("palavra", "PaLaVRa"),
	("aeiou ou", "aeiou ou"),
	("bcdfgh jklmn", "BCDFGH JKLMN"),
	("exemplo de frase", "eXeMPLo De FRaSe"),
]


for i, test in enumerate(test_cases):
	test_case = deepcopy(test)
	try:
		with timeout(seconds=1):
			result = main(test)
		if(test_case[-1] != result):
			print(f'{i+1} | {test_case[:-1]} => {test_case[-1]} != {result}')
		#else:
		#	print(f'{i+1} | {test_case[:-1]} => PASSED')
	except Exception as err:
		print(f'{i+1} | {test_case[:-1]} => {test_case[-1]} != {type(err)}: {err}')
		
#python3 test_function.py		

