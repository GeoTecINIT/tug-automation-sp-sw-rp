import os
import json


def list_folder(path):
    subjects = os.listdir(path)
    subjects.sort()
    return subjects


def list_subjects_folders(path):
    subjects = list_folder(path)
    return list(filter(lambda name : os.path.isdir(os.path.join(path, name)) and name.startswith('s'), subjects))


def load_json(data_file_path):
    with open(data_file_path, 'r') as file:
        return json.load(file) 
    
    
def to_json(data, data_file_path):
    with open(data_file_path, 'w') as file:
        json.dump(data, file)