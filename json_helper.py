import json
import os


def read_json (file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def read_all_json (file_path):
    all_list = []
    for file in os.listdir(file_path):
        new_file_path = "%s/%s" % (file_path, file)
        data = read_json(new_file_path)
        all_list.append(data)
    return all_list



        # for key, value in data.items():
        #     print(f"{key}: {value}")

read_all_json('/Users/jim/Projects/p1/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')

