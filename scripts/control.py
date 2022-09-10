import argparse
import os
from datetime import date
import random
import json
import ast

try:
    import pyinputplus as pyip
except:
    os.system("pip install pyinputplus")
    import pyinputplus as pyip



def update_json(filename, entry):
    with open(filename, "r+") as file:
        data = json.load(file)
        data.insert(0,entry)
        file.seek(0)
        json.dump(data, file)

def remove_from_json(name):
    data = []
    with open('../json/{}.json'.format(name), "r+") as file:
        data = json.load(file)
        print(data)
        bm = ast.literal_eval(pyip.inputMenu([str(d) for d in data], lettered=True, blank=True))
        for i, j in enumerate(data):
            if j == bm:
                data.pop(i)
                break
    with open('../json/{}.json'.format(name), "w") as file:
        json.dump([], file)
    for i in data:
        update_json('../json/{}.json'.format(name), i)

def generate_blogfile():
    today = date.today()
    t = today.strftime("%b-%d-%Y")
    id = random.randint(0,100)
    new_filename = str(t)+"-"+str(id)+".txt"
    filenames = [f for f in os.listdir("./blogs")]
    print(filenames)
    if new_filename in filenames:
        generate_blogfile()
    else:
        text = "Title Here\n---\n{}\n---\nType Here".format(t)
        os.system("touch ./blogs/{}".format(new_filename))
        os.system('echo "{}" >> ./blogs/{}'.format(text, new_filename))
        return new_filename

def update_blog(filename):
    f = open(filename, "r")
    parts = [l.replace("\n","") for l in f.read().split("---")]
    entry = {
        "title" : parts[0],
        "date" : parts[1],
        "content" : parts[2]
    }
    update_json('../json/blogs.json', entry)

def write():
    filename = generate_blogfile()
    os.system("gedit ./blogs/{}".format(filename))
    update_blog("./blogs/{}".format(filename))

def edit():
    filename = pyip.inputStr("Enter filename : ")
    os.system("gedit ./blogs/{}".format(filename))
    update_blog("./blogs/{}".format(filename))

def update_all_blogs():
    with open('../json/blogs.json', "w") as file:
        json.dump([], file)
    filenames = [f for f in os.listdir("./blogs")]
    for filename in filenames:
        update_blog("./blogs/{}".format(filename))

def bookmark():
    type = pyip.inputMenu(['Youtube', 'Twitter', 'Instagram', 'Others'], lettered=True)
    hastitle = pyip.inputYesNo("Do u need to add title ? ")
    title = None
    if hastitle == "yes":
        title = pyip.inputStr("Enter the title :  ")
    hasDescription = pyip.inputYesNo("Do u need to add description ? ")
    description = None
    if hasDescription == "yes":
        description = pyip.inputStr("Enter the description :  ")
    link = pyip.inputStr("Enter link : ")

    entry = {
        "title" : title,
        "description" : description,
        "type" : type,
        "link" : link
    }
    update_json('../json/bookmarks.json', entry)

def remove_bookmark():
    remove_from_json("bookmarks")

def add_to_my_details():
    entry = {
        "detail" : pyip.inputStr("Enter the detail :  ")
    }
    update_json('../json/details.json', entry)

def remove_from_my_details():
    remove_from_json("details")

def push():
    os.system("cd .. ; ls; git add json; git status; git push -f")
    
my_parser = argparse.ArgumentParser(description='Helper for updating static page akshaj000.github.io')
my_parser.add_argument('-d','--addtomydetails', help='Add to mydetail', const=True, nargs="?")
my_parser.add_argument('-dr','--removefrommydetails', help='Remove from mydetails', const=True, nargs="?")
my_parser.add_argument('-w','--write', help='Write a new blog', const=True, nargs="?")
my_parser.add_argument('-e','--edit', help='Edit already exisiting blog', const=True, nargs="?")
my_parser.add_argument('-u','--update', help='Update all exisiting blog', const=True, nargs="?")
my_parser.add_argument('-b','--bookmark', help='Bookmark something', const=True, nargs="?")
my_parser.add_argument('-br','--remove_bookmark', help='Remove bookmark', const=True, nargs="?")
my_parser.add_argument('-push', help="push to github", const=True, nargs="?")
args=my_parser.parse_args()

print("\n")
if args.write:
    write()
elif args.bookmark:
    bookmark()
elif args.remove_bookmark:
    remove_bookmark()
elif args.edit:
    edit()
elif args.update:
    update_all_blogs()
elif args.addtomydetails:
    add_to_my_details()
elif args.removefrommydetails:
    remove_from_my_details()
elif args.push:
    push()
