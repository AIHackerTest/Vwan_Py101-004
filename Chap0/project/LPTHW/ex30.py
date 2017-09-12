people = 20
cats = 40
dogs = 15
if people > cats:
    print ("Too many cats! The world is doomed!" )
elif people < cats:
    print ("Not many cats! The world is saved!" )
else:
    print ("We cannot decide")

if people < dogs:
    print ("The world is drooled on!" )
elif people > dogs: 
    print ("The world is dry!" )
    dogs += 5
else:
    print ("People are greater than or equal to dogs." )
