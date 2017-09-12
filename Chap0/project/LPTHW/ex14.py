from sys import argv
script, user_name,pwd=argv

prompt="> "
print ("Hi %s, I'm the %s script, my pwd is %s" % (user_name,script,pwd))
likes=input(prompt)

computer = input(prompt)
print ("%s,%r" % (likes,computer ))
