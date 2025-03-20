import json

def read_json (file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        return data


        # for key, value in data.items():
        #     print(f"{key}: {value}")

read_json('/Users/jim/Projects/p1/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json')