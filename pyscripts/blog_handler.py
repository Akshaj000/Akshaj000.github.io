import json, os, random
from datetime import date
import pyinputplus as pyip
from sqlalchemy import true
from .utils import update_json, remove_from_json

def generate_blogfile():
    today = date.today()
    t = today.strftime("%b-%d-%Y")
    id = random.randint(0,100)
    new_filename = str(t)+"-"+str(id)+".md"
    filenames = [f for f in os.listdir("./blogs")]
    print(filenames)
    if new_filename in filenames:
        generate_blogfile()
    else:
        text = "# Title Here\n#### {}\nType Here".format(t)
        os.system("touch ./blogs/{}".format(new_filename))
        os.system('echo "{}" >> ./blogs/{}'.format(text, new_filename))
        return new_filename

def update(filename):
    entry = {
        "file" : filename.split("/")[2]
    }
    update_json('./json/blogs.json', entry)


def update_blog():
    with open('./json/blogs.json', "w") as file:
        json.dump([], file)
    filenames = [f for f in os.listdir("./blogs")]
    for filename in filenames:
        update("./blogs/{}".format(filename))

def write_blog():
    filename = generate_blogfile()
    os.system("gedit ./blogs/{}".format(filename))
    update("./blogs/{}".format(filename))

def edit_blog():
    filenames = [f for f in os.listdir("./blogs")]
    filename = pyip.inputMenu(filenames,lettered=True)
    os.system("gedit ./blogs/{}".format(filename))
    update_blog()

def remove_blog():
    filenames = [f for f in os.listdir("./blogs")]
    filename = pyip.inputMenu(filenames,lettered=True)
    os.system("rm -r ./blogs/{}".format(filename))
    update_blog()


__all__=[
    'write_blog',
    'edit_blog',
    'update_blog',
    'remove_blog'
]