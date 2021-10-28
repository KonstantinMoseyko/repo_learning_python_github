from os import path, walk, listdir
import shutil

my_project_name = 'my_project'

try:
    for root, directories, names_files in walk(my_project_name):
        if 'templates' in directories and root != my_project_name:
            for entrance in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entrance),
                                path.join(my_project_name, 'templates', path.basename(root)))
except FileExistsError:
    print("Файлы уже существуют")
