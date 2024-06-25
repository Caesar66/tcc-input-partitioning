from save_tests_output_main import main
from itertools import product
import multiprocessing as mp
import time

problem_ids = [736, 742, 744, 751, 798, 800, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 827, 828, 829, 831, 832, 833, 834, 835, 836, 838, 839, 840, 842]
criteria = ["original", "input", "new_input"]

#problem_ids = [736]
#criteria = ["new_input"]
executions = []
for args in product(criteria, problem_ids):
    permutation = [args[0],args[1]]
    executions.append(permutation)

start = time.time()

number_processes = mp.cpu_count()-1 if mp.cpu_count()-1>0 else 1

for i in executions:
    main(i[0],i[1], number_processes)

end = time.time()
print('{:.4f} s'.format(end-start))
