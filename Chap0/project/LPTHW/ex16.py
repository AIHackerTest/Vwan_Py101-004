from sys import argv

script, filename=argv

input("?")
target = open(filename,"w")

target.truncate()

line1=input("line 1:")
line2=input("line 2:")

target.write(line1+"\n")
target.write(line2+"\n")

target.close()
