import os


def create_folder(workspace, folder):
    path = os.path.join(workspace, folder)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"create folder with path {path}")
    else:
        print(f"folder exists {path}")


create_folder('my_project', 'settings')
create_folder('my_project', 'mainapp')
create_folder('my_project', 'adminapp')
create_folder('my_project', 'authapp')
