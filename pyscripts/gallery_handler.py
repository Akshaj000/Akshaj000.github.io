import pyinputplus as pyip
from .utils import update_json, remove_from_json

def check_drive_link(link):
    if "https://drive.google.com/file/d/" in link:
        link = "https://drive.google.com/uc?export=view&id={}".format(link.split("/")[5])
    return link

def add_to_gallery():
    entry = {
        "source" : check_drive_link(pyip.inputURL("Enter the source link :  "))
    }
    update_json('./json/gallery.json', entry)

def remove_from_gallery():
    remove_from_json("gallery")


__all__ = [
    'add_to_gallery',
    'remove_from_gallery'
]