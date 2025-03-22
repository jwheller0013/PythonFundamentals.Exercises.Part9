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

def write_pickle(file_path, data):
    json_object = json.dumps(data)
    with open("super_smash_characters.pickle", mode = "w") as outfile:
        outfile.write(json_object)

def load_pickle(file_path):
    with open(file_path, 'r') as file:
        pickle = json.load(file)
    print(pickle)

        # for key, value in data.items():
        #     print(f"{key}: {value}")

# data = read_all_json('/Users/jim/Projects/p1/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
#
# write_pickle('/Users/jim/Projects/p1/PythonFundamentals.Exercises.Part9/data/super_smash_bros/', data)
