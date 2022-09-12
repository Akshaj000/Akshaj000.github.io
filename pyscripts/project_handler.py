import pyinputplus as pyip
from .utils import update_json, remove_from_json

def add_project():
    repository = pyip.inputURL("Enter the repository link : ")
    title =  pyip.inputStr("Enter title : ")
    description = pyip.inputStr("Enter description : ")
    image = pyip.inputURL("Enter image URL : ")
    entry = {
        "repository" : repository,
        "title" : title,
        "description" : description,
        "image" : image
    }
    update_json('./json/projects.json', entry)


def remove_project():
    remove_from_json("projects")


__all__=[
    'add_project',
   'remove_project'
]