from sys import argv
from os.path import exists

script,file1,file2=argv

indata=open(file1).read()

print (" the length of inpt file %r" % len(indata))
print ("does input file exists? %r" % exists(file2))

input()

outfile = open(file2,"w")
outfile.write(indata)

outfile.close()
