def gold_room():
    print ("This room is full of gold. How much do you take?")

    next = input("> ")
   # if isinstance(next,int):
    if type(next) == type(1):
        how_much=int(next)
    else:
        print ("Man, type a number pls")

def dead(why):
    print (why, "Good Job")
    exit(0)

def bear_room():
    print ("""
            There is a bear here. The bear has a bunch of honey. The fat bear is in front of another door. How are you going to move the bear?
            """)
    moved = False
    while not moved:
        next = input("> ")
        if next =="take honey":
            dead("You are eaten by the bear")
        elif next == "taunt bear":
            print ("bear moved")
            moved=True
            gold_room()
        else:
            print ("i am lost")

def cthu_room():
    next = input("> ")
    if "flee" in next:
        start()
    else:
        cthu_room()

def start():
    print ("You are in a dark room")
    print ("There is a door to your right and left")
    print ("which one do you take?")

    prompt = "> "

    direction = input(prompt)

    if direction == "left":
        bear_room()
    elif direction == "right":
        cthu_room()
    else:
        dead("You stumble aournd the room until you starve")

start()
