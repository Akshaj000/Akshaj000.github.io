import pyinputplus as pyip
from .utils import update_json, remove_from_json

def bookmark():
    type = pyip.inputMenu(['youtube', 'twitter', 'instagram', 'other'], lettered=True)
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
    update_json('./json/bookmarks.json', entry)

def remove_bookmark():
    remove_from_json("bookmarks")


__all__ = [
    'bookmark',
    'remove_bookmark'
]