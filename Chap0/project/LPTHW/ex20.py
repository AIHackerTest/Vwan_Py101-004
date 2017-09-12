#from sys import argv
#script,filename=argv
filename = "c:\\temp\\page1.html"
def print_all(f):
	print (f.read())

def rewind(f):
	f.seek(100)

def print_a_line(line_count,f):
	print (line_count,f.readline())

current_file=open(filename,'r',-1,'utf-8')

print_all(current_file)
rewind(current_file)
print_a_line(1,current_file)
