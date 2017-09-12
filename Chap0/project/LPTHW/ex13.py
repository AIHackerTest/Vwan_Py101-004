from sys import argv

script,first,second,third=argv
print (type(argv))
print ("script is called:",script)
print ("argv is called: ", argv)
print ("first variable is called: ", first)
print ("second variable is called: ", second)
print ("third variable is called: ", third)

rwinput = input("is this raw input?:")
print (rwinput)
