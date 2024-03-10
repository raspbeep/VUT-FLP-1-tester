import os
import subprocess
import sys

from config import N_TESTS, TASK_2_CLASSIFICATIONS
from generate_tests import generate
from import_gini import module as g
# import gini as g

total_count_1 = 0
total_count_correct_1 = 0

total_test_2_count = 0
total_test_2_correct_count = 0

def test_if_present(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"No file found at {filepath}")
    else:
        print(f"File found at {filepath}")

def check_output(out_script, expected, idx):
    global total_count_correct_1, total_count_1
    total_count_1 += 1
    if out_script == expected:
        print(f' [ OK ] - correctly classified all data')
        total_count_correct_1 += 1
    else:
        print(f' [ BAD ] - test case: {idx}')
        print('##### EXPECTED #####')
        print(expected)
        print('##### ACTUAL #####')
        print(out_script)
        raise Exception("Invalid classification")

def run_task_1(idx):
    try:
        command = ["./flp-fun", "-1", "./tests/trees/tree_" + str(idx), "./tests/new_data/new_data_" + str(idx)]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise ('flp-fun exited with non-zero return code')
        with open (f'./tests/classifications/classification_{idx}', 'r') as expected:
            # WINLUL CHANGE LINE HERE
            # check_output("\n".join(result.stdout.decode().splitlines()), expected.read().strip(), idx)
            check_output(result.stdout.decode(), expected.read().strip(), idx)
            

    except subprocess.CalledProcessError as e:
        print(f"Error executing shell script: {e.stderr.decode()}", file=sys.stderr)
        raise Exception
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        raise Exception
    
def run_task_2(idx):
    global total_test_2_correct_count, total_test_2_count
    try:
        command = ["./flp-fun", "-2", f'./tests/training_data/data_{str(idx)}']
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise ('flp-fun exited with non-zero return code')

        t_expected = g.parse_tree_from_file(f'./tests/trees/tree_{idx}')[0]
        t_parsed = g.parse_tree_from_string(result.stdout.decode())[0]
        
        count_correct = 0
        count_total = TASK_2_CLASSIFICATIONS

        test_data = g.create_dataset(n_samples=count_total)
        classes_from_expected = g.classify_new_data(t_expected, test_data)
        classes_from_parsed = g.classify_new_data(t_parsed, test_data)
        
        for i in range(count_total):
            if classes_from_expected[i] == classes_from_parsed[i]:
                count_correct += 1
        total_test_2_count += count_total
        total_test_2_correct_count += count_correct

        if count_correct != count_total:
            print(f' number of equal classifications compared to reference tree: {count_correct}/{count_total} ({(count_correct / count_total) * 100}%)')
        else:
            print(f' [ OK ] - all {count_total} classified correctly')

    except subprocess.CalledProcessError as e:
        print(f"Error executing shell script: {e.stderr.decode()}", file=sys.stderr)
        raise Exception
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        raise Exception
    
def make_files():
    command = ['make']
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception("Cannot make files")

if __name__ == "__main__":
    generate(N_TESTS)

    try:
        test_if_present('Makefile')
        test_if_present('flp-fun.hs')
        make_files()
        test_if_present('flp-fun')
        for i in range(1, N_TESTS + 1):
            print(f'Test #{i}')
            print('Task 1:', end='')
            run_task_1(i)
            print('Task 2:', end='')
            run_task_2(i)
            print('----------')
        if total_count_1 != 0:
            print(f'Task 1 classified correctly {(total_count_correct_1 / total_count_1)*100}% ({total_count_correct_1}/{total_count_1})')
        if total_test_2_count != 0:
            print(f'Task 2 classified correctly {(total_test_2_correct_count / total_test_2_count)*100}% ({total_test_2_correct_count}/{total_test_2_count})')
        
    except Exception as e:
        print(e)
