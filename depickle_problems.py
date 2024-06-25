import pickle
import os
import pandas as pd
import shutil

#Problemas e criterios
problem_ids = [736, 742, 744, 751, 798, 800, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 827, 828, 829, 831, 832, 833, 834, 835, 836, 838, 839, 840, 842]
criteria = ["original","input", "new_input"]

#Caminho da pasta CSV
directory = os.getcwd()
path_csv =  os.path.join(directory, "CSV")
os.makedirs(path_csv, exist_ok=True)


for problem_id in problem_ids:
	path_csv_solution =  os.path.join(path_csv, f"solution_{problem_id}.csv")
	values_solution = pd.DataFrame({'solution_id': pd.Series(dtype='int'), 'problem_id': pd.Series(dtype='int')})
	for criterion in criteria:
		values_solution[f'{criterion}_outcome'] = pd.Series(dtype='bool_')
		values_solution[f'{criterion}_result'] = pd.Series(dtype='str')
				
		#os.makedirs(os.path.dirname(path_csv_solution), exist_ok=True)
	values_solution.to_csv(path_csv_solution, index=False)

with open('problems.pkl', 'rb') as f:
	data = pickle.load(f)

	#Pega diretorios de pastas e do confteste
	path_src = os.path.join(directory, "tests")
	path_src_conf = os.path.join(path_src, "conftest.py")


	for enunciado in data:
		#Pega o numero do problema
		name_id = str(enunciado["id"])
		name_id_txt = name_id + ".txt"

		#Pega o caminho aonde estao os testes
		path_src_problem = os.path.join(path_src, name_id)

		#Pega o caminho onde o enunciado vai ficar
		path = os.path.join(directory, "problems")
		path = os.path.join(path, name_id)
		path_txt = os.path.join(path, name_id_txt)
		os.makedirs(os.path.dirname(path_txt), exist_ok=True)#Garante que o caminho existe

		#Pega o caminho onde os testes e o conftest vao ficar e os coloca lá
		path_conf = os.path.join(path, "conftest.py")
		shutil.copy(path_src_conf, path_conf)
		for criterion in criteria:
			path_src_test = os.path.join(path_src_problem, f"test_{criterion}_{name_id}.py")
			path_test = os.path.join(path, f"test_{criterion}_{name_id}.py")
			shutil.copy(path_src_test, path_test)

		#Escreve o eneunciado
		with open(path_txt, 'w', encoding="utf-8") as g:
			g.write("chapter__label:")
			g.write('\n')
			g.write(enunciado["chapter__label"])
			g.write('\n')
			g.write("id:")
			g.write('\n')
			g.write(str(enunciado["id"]))
			g.write('\n')
			g.write("content:")
			g.write('\n')
			g.write(enunciado["content"])
			g.write('\n')
			g.write('\n')
