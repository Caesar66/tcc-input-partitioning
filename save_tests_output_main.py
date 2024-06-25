import os
import sys
import subprocess
import pytest
import pandas as pd
from tqdm import tqdm
import importlib

import math
import multiprocessing as mp
import warnings

#Fixed: path, path_test, problem_id, criterion, test_cases, processes_ids, lock
#Mutable: solution_filename
def save_tests_output(args):
	solution_filenames, path, path_test, problem_id, criterion, process_id, solutions_check_json  = args
	
	results = []
	
	for solution_filename in tqdm(solution_filenames, total=len(solution_filenames)):
		#Extract solution id
		solution_id = solution_filename[9:-3]
		
		# Find the next available process ID
#		process_id = None
#		with lock:
#			for key, value in processes_ids.items():
#				if value:
#					process_id = key
#					processes_ids[key] = False  # Mark it as occupied
#					break
					
		#Path of the JSON report
		if solution_id in solutions_check_json:
			path_json = os.path.join(path, f"log_{criterion}_{solution_id}.json")
		else:
			path_json = os.path.join(path, f"log_{criterion}_{process_id}.json")
		#path_json = os.path.join(path, f"log_{criterion}_{solution_id}.json")
		
		#Run subprocess that creates a JSON report of the results
		subprocess.run(f"python3 -m pytest {path_test} --tb=no --show-capture=no --solution=solution_{solution_id} --report-log={path_json} --timeout=1", shell=True, stdout=subprocess.DEVNULL)
		
		#tests_results is the string composed of each individual test result
		tests_results = ''
		#new_outcome is the new outcome of the tests (default is passed)
		new_outcome = 1
		#Parses the JSON file 
		with open(path_json, 'r') as log:
			for node in log:
				node = node.lower()
				#This is the "node" in which the test actually occurs
				if '\"when\": \"call\"' in node:
					if 'passed' in node:
						tests_results += 'P'
					else:
						if 'assert' in node:
							tests_results += 'F'
						elif 'timeout' in node:
							tests_results += 'T'
						else:
							tests_results += 'E'
						new_outcome = 0
				
#		#Only one process is allowed to write per time
#		with lock:
#			processes_ids[process_id] = True
		results.append((solution_id, new_outcome, tests_results))
		
	#return (solution_id, new_outcome, tests_results)
	return results
	
#Generator function to create chunks on the solution_filenames array
def chunk_gen(size, workers):
	chunk = math.ceil(size/workers)
	
	yield chunk
	while chunk < size:
		size = size - chunk
		workers = workers - 1
		chunk = math.ceil(size/workers)
		
		yield chunk

def main(criterion, problem_id, number_processes):
	#Get the main directory path
	directory = os.getcwd()
	
	#Directory of the folder with the CSV collectibles (solution and tests)
	path_csv = os.path.join(directory, "CSV")
	
	#Path to the "solution" spreadsheet, to register every solution result
	path_csv_solution = os.path.join(path_csv, f"solution_{problem_id}.csv")
	
	#Edits the dataframe if criterion == original
	df_solution = pd.read_csv(path_csv_solution)
	if(criterion == 'original' and 'original_outcome' not in df_solution.columns):
		df_solution = df_solution.rename(columns={'old_outcome':'original_outcome'})
		df_solution.insert(5, 'original_result', pd.NA)
		df_solution.to_csv(path_or_buf=path_csv_solution, index=False)
	
	#Path to the the folder with all the "solutions" needed to be run
	path = os.path.join(directory, "problems")
	path = os.path.join(path, str(problem_id))

    #Sorted list of all solutions ids
	pwd_list = sorted([x for x in os.listdir(path) if "solution_" in x])
	#Creates chunks approximately of same size to distribute among processes
	solution_filenames = [pwd_list[i*chunk:(i+1)*chunk] for i, chunk in enumerate(chunk_gen(len(pwd_list), number_processes))]
    
    #Path to the file with the case tests
	test_str = f"test_{criterion}_{problem_id}.py"
	path_test = os.path.join(path, test_str)

    #Loads the test
#	spec = importlib.util.spec_from_file_location(test_str, path_test)
#	test = importlib.util.module_from_spec(spec)
#	sys.modules["module.name"] = test
#	
#	#Executes the module to get number of test_cases
#	spec.loader.exec_module(test)
#	test_cases = len(test.test_cases)
	
	print(f'Exercise: {problem_id}\nCriterion: {criterion}\nTotal Files: {len(pwd_list)}\nNumber of Workers: {number_processes}')
	
	#solutions_check_json = ['173555', '173683', '173684', '176261', '177933', '178486', '178487', '179409', '180471', '180900', '181923', '181942', '182353']
	solutions_check_json = []
	
#	with mp.Manager() as manager:
#				
#		#Create a dicitonary for the processes spots and ids for managing the report logs
#		processes_spots = manager.dict()
#		for spot in range(number_processes):
#			processes_spots[spot] = True
#
#		#Lock used for managing the processes spots
#		lock = manager.Lock()
#		
#		#args_ = [path, path_test, problem_id, criterion, test_cases, processes_spots, lock]
#
#		with mp.Pool(processes=number_processes) as pool:
#
#			#Gets the list with the result for treatment
#			#for result in tqdm(pool.imap_unordered(save_tests_output, [[solutions_chunk] + args_ for solutions_chunk in solution_filenames]), total=len(pwd_list)):
#			for results in pool.imap_unordered(save_tests_output, [[solutions_chunk, path, path_test, problem_id, criterion, test_cases, process_id] for solutions_chunk, process_id in zip(solution_filenames, range(1, number_processes+1))]):
#				#os.remove(os.path.join(path, f'log_{criterion}_{result[0]}.json'))
#				
#				#Suppress FutureWarning about column data types
#				with warnings.catch_warnings():
#					warnings.simplefilter(action='ignore', category=FutureWarning)
#					#Inputs the value of the result based on the criteria unto the dataframe
#					for result in results:
#						df_solution.loc[df_solution['solution_id'] == int(result[0]), [f'{criterion}_outcome',f'{criterion}_result']] = bool(result[1]), result[2]
#							#Writes the both main dataframe to their respective csv file

	with mp.Pool(processes=number_processes) as pool:

		#Gets the list with the result for treatment
		#for result in tqdm(pool.imap_unordered(save_tests_output, [[solutions_chunk] + args_ for solutions_chunk in solution_filenames]), total=len(pwd_list)):
		for results in pool.imap_unordered(save_tests_output, [[solutions_chunk, path, path_test, problem_id, criterion, process_id, solutions_check_json] for solutions_chunk, process_id in zip(solution_filenames, range(1, number_processes+1))]):
			#os.remove(os.path.join(path, f'log_{criterion}_{result[0]}.json'))
			
			#Suppress FutureWarning about column data types
			with warnings.catch_warnings():
				warnings.simplefilter(action='ignore', category=FutureWarning)
				#Inputs the value of the result based on the criteria unto the dataframe
				for result in results:
					df_solution.loc[df_solution['solution_id'] == int(result[0]), [f'{criterion}_outcome',f'{criterion}_result']] = bool(result[1]), result[2]
						#Writes the both main dataframe to their respective csv file
						
	df_solution.to_csv(path_or_buf=path_csv_solution, index=False)

if __name__ == '__main__':
	main(criterion, problem_id, number_processes)
