import argparse
from pyscripts import*
    
my_parser = argparse.ArgumentParser(description='Helper for updating static page akshaj000.github.io')
my_parser.add_argument('-d','--addtomydetails', help='Add to mydetail', const=True, nargs="?")
my_parser.add_argument('-dr','--removefrommydetails', help='Remove from mydetails', const=True, nargs="?")
my_parser.add_argument('-w','--write', help='Write a new blog', const=True, nargs="?")
my_parser.add_argument('-e','--edit', help='Edit already exisiting blog', const=True, nargs="?")
my_parser.add_argument('-u','--update', help='Update all exisiting blog', const=True, nargs="?")
my_parser.add_argument('-r','--remove', help='Delete exisiting blog', const=True, nargs="?")
my_parser.add_argument('-b','--bookmark', help='Bookmark something', const=True, nargs="?")
my_parser.add_argument('-br','--remove_bookmark', help='Remove bookmark', const=True, nargs="?")
my_parser.add_argument('-g','--addtogallery', help='Add to gallery', const=True, nargs="?")
my_parser.add_argument('-gr','--removefromgallery', help='Remove from gallery', const=True, nargs="?")
my_parser.add_argument('-p','--addproject', help='Add new project', const=True, nargs="?")
my_parser.add_argument('-pe','--editproject', help='Edit existing project', const=True, nargs="?")
my_parser.add_argument('-pu','--updateproject', help='Update existing projects', const=True, nargs="?")
my_parser.add_argument('-pr','--removeproject', help='Remove project', const=True, nargs="?")
my_parser.add_argument('-push', help="push to github", const=True, nargs="?")

args=my_parser.parse_args()
cases = {
    args.write : write_blog,
    args.remove_bookmark : remove_bookmark,
    args.edit : edit_blog,
    args.remove : remove_blog,
    args.update : update_blog,
    args.addtomydetails : add_to_my_details,
    args.removefrommydetails : remove_from_my_details,
    args.addtogallery : add_to_gallery,
    args.removefromgallery : remove_from_gallery,
    args.addproject : add_project,
    args.editproject : edit_project,
    args.removeproject : remove_project,
    args.updateproject : update_project,
    args.push : push,
}

for argument in cases:
    if argument : cases[argument]()
