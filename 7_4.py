import os
from collections import defaultdict


def directory_info():
    root_directory = 'my_project'
    some_files_dict = defaultdict(int)
    for root, directory, names_files in os.walk(root_directory):
        for file in names_files:
            size_file = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            some_files_dict[size_file] += 1

    for size_file, nums_val in sorted(some_files_dict.items()):
        print(f'{size_file}: {nums_val}')


directory_info()
