import os

def create_project_file(project_name):
    file_name = project_name + '.txt'
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as fp:
            pass


def append_to_file(project_name, data):
    with open(project_name, 'a') as file:
        file.write(data+'\n')

