import imp
import pyinputplus as pyip
from .utils import update_json, remove_from_json

def add_to_my_details():
    entry = {
        "detail" : pyip.inputStr("Enter the detail :  ")
    }
    update_json('./json/details.json', entry)

def remove_from_my_details():
    remove_from_json("details")

__all__ = [
    'add_to_my_details',
    'remove_from_my_details'
]