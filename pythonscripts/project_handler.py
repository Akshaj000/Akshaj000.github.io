import json, os, random
from datetime import date
import pyinputplus as pyip
from .utils import update_json, remove_from_json

def generate_projectfile():
    today = date.today()
    t = today.strftime("%b-%d-%Y")
    id = random.randint(0,100)
    new_filename = str(t)+"-"+str(id)+".txt"
    filenames = [f for f in os.listdir("./projects")]
    if new_filename in filenames:
        generate_projectfile()
    else:
        text = "Title Here \n---\nimage url here \n---\nrepo link here \n---\n Type about your project here".format(t)
        os.system("touch ./projects/{}".format(new_filename))
        os.system('echo "{}" >> ./projects/{}'.format(text, new_filename))
        return new_filename

def update(filename):
    file = open(filename,"r")
    parts = [f.strip() for f in file.read().split("---")]
    entry = {
        "repository" : parts[2],
        "title" : parts[0],
        "description" : parts[3],
        "image" : parts[1]
    }
    update_json('./json/projects.json', entry)

def update_project():
    with open('./json/projects.json', "w") as file:
        json.dump([], file)
    filenames = [f for f in os.listdir("./projects")]
    for filename in filenames:
        update("./projects/{}".format(filename))

def add_project():
    filename = generate_projectfile()
    os.system("gedit ./projects/{}".format(filename))
    update("./projects/{}".format(filename))

def edit_project():
    filenames = [f for f in os.listdir("./projects")]
    filename = pyip.inputMenu(filenames,lettered=True, blank=True)
    os.system("gedit ./projects/{}".format(filename))
    update_project()

def remove_project():
    filenames = [f for f in os.listdir("./projects")]
    filename = pyip.inputMenu(filenames,lettered=True, blank=True)
    os.system("rm -r ./projects/{}".format(filename))
    update_project()


__all__=[
    'add_project',
    'edit_project',
   'remove_project',
   'update_project'
]