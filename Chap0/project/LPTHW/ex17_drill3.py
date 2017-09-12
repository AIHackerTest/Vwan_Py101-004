from sys import argv
from os.path import exists

script,file1,file2=argv

if (not exists(file2)):
    with open(file2,"w") as file:
        file.write(open(file1).read())
