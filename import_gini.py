import importlib
import sys

filepath='./__pycache__/gini.cpython-311.pyc'
spec = importlib.util.spec_from_file_location("gini", filepath)
module = importlib.util.module_from_spec(spec)
sys.modules["gini"] = module
spec.loader.exec_module(module)

if __name__ == '__main__':
    print(module.create_class_list())