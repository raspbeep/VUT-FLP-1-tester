import os

from config import N_SAMPLES_TREE, NEW_DATA_COUNT, FEATURE_SIZE
from import_gini import module as g
# from gini import (classify_new_data, construct_tree, create_class_list,
#                   create_dataset, print_tree, FEATURE_SIZE)

def remove_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            remove_directory(file_path)
    os.rmdir(directory)
    
def create_clean_dirs():
    if os.path.exists('./tests'):
        remove_directory('./tests')
    os.makedirs('./tests/training_data')
    os.makedirs('./tests/trees')
    os.makedirs('./tests/new_data')
    os.makedirs('./tests/classifications')

def print_training_data_into_file(training_data, idx):
    with open(f'./tests/training_data/data_{idx}', 'w') as f:
        for dato in training_data:
            for val in dato[0]:
                print(val, end=',', file=f)
            print(dato[-1], file=f)

def print_tree_into_file(t, idx):
    with open(f'./tests/trees/tree_{idx}', 'w') as f:
        g.print_tree(t, file=f)

def print_new_data_into_file(new_data, idx):
    with open(f'./tests/new_data/new_data_{idx}', 'w') as f:
        for dato in new_data:
            for val in dato[:-1]:
                print(val, end=',', file=f)
            print(dato[-1], file=f)

def print_classifications_into_file(classifications, idx):
    with open(f'./tests/classifications/classification_{idx}', 'w') as f:
        for class_name in classifications:
            print(class_name, file=f)


def generate_test(idx, feature_size=FEATURE_SIZE, n_samples_tree=N_SAMPLES_TREE, new_data_count=NEW_DATA_COUNT):
    ds = g.create_dataset(n_samples=n_samples_tree, feature_size=feature_size, class_list=g.create_class_list(n_classes=10))
    
    print_training_data_into_file(ds, idx)

    t = g.construct_tree(ds)
    print_tree_into_file(t, idx)
    
    new_data = g.create_dataset(n_samples=new_data_count, feature_size=feature_size)
    print_new_data_into_file(new_data, idx)

    classifications = g.classify_new_data(t, new_data)
    print_classifications_into_file(classifications, idx)


def generate(test_count=10):
    create_clean_dirs()
    
    for i in range(1, test_count + 1):
        generate_test(i)
