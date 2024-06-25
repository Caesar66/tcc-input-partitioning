import pickle
import pandas as pd
from tqdm import tqdm
import os
import mysql.connector

problem_ids = [736, 742, 744, 751, 798, 800, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 827, 828, 829, 831, 832, 833, 834, 835, 836, 838, 839, 840, 842]
#problem_ids = [736]
#criteria = ["original", "input", "new_input"]

directory = os.getcwd()


with open('solutions.pkl', 'rb') as f:
	data = pickle.load(f)

	#create_import_stmts()
	values=[]
	for i, enunciado in enumerate(tqdm(data)):
		problem_id = str(enunciado["problem_id"])
		solution_id = f"solution_{i+1}"
		solution_id_path = f"solution_{i+1}.py"
		path = os.path.join(directory, "problems")
		path = os.path.join(path, problem_id)
		path_id = os.path.join(path, solution_id_path)

		if not os.path.exists(path):
			os.makedirs(path)

		values.append((i+1, enunciado["problem_id"]))
	
		with open(path_id, 'w', encoding="utf-8") as g:
			g.write(enunciado["solution"])

	for i, problem_id in enumerate(tqdm(problem_ids)):
		path_csv = os.path.join(directory, "CSV")
		path_csv = os.path.join(path_csv, f"solution_{problem_id}.csv")

		df_solution = pd.read_csv(path_csv)

		df_solution = df_solution.iloc[0:0]

		values_temp = list(filter(lambda x: x[1] == problem_id, values))
		df_value = pd.DataFrame(values_temp, columns=['solution_id','problem_id'])
		df_solution = pd.concat([df_solution, df_value], ignore_index=True)
		df_solution.to_csv(path_or_buf=path_csv, index=False)




