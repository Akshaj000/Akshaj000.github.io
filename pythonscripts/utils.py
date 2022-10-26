import json, os, ast
import pyinputplus as pyip

def update_json(filename, entry):
    contains = False
    with open(filename, "r+") as file:
        data = json.load(file)
        for j in data:
            if j == entry:
                contains = True
                break

    if not contains:
        with open(filename, "r+") as file:
            data = json.load(file)
            data.append(entry)
            file.seek(0)
            json.dump(data, file)
    else:
        print("already exist")

def remove_from_json(name):
    data = []
    with open('./json/{}.json'.format(name), "r+") as file:
        data = json.load(file)
        print(data)
        bm = ast.literal_eval(pyip.inputMenu([str(d) for d in data], lettered=True, blank=True))
        for i, j in enumerate(data):
            if j == bm:
                data.pop(i)
                break
    with open('./json/{}.json'.format(name), "w") as file:
        json.dump([], file)
    for i in data:
        update_json('./json/{}.json'.format(name), i)

def push():
    os.system("git add json; git status; git push -f")

__all__ =  [
    'update_json',
    'remove_from_json',
    'push'
]