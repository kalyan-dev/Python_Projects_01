# Create a commandline tool
#  >> searchstring.py dir string
#  search everyfile in the directory for the string, and display the file name;


import sys
import os

search = sys.argv[2]
folder = sys.argv[1]

tree = os.walk(folder)

for (dirname, folders, files) in tree:
    for file in files:
        with open(dirname+"\\"+file,"rt") as f:
            if search in f.read():
                print(dirname + "\\" + file)


