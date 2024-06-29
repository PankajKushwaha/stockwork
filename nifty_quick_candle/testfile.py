import os

def get_list_of_all_file(folder):
    for path, subdirs, files in os.walk(folder)
        for name in files:
            print(os.path.join(path, name))
