from sys import argv

script, filename=argv

txt = open(filename)

print ("your file is: %s" % filename)

print (txt.read())

file_again = input("> ")
txt_again = open(file_again)

print (txt_again.read())
