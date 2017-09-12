things="Apples Oranges Crows Telephone Light Sugar"

stuff=things.split(" ")

more=["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
	next=more.pop()
	print ("next is %s" % next)
	stuff.append(next)

print (stuff)

print (stuff[1])
print (stuff[-1])
print (stuff.pop())
print (' '.join(stuff))
print ('#'.join(stuff[3:5]))
