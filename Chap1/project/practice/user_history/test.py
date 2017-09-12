from user import User
from history import History

user1 = User("user1","pass1")
user2 = User("user2","pass2")

print(hash(user1.history))
print(hash(user2.history))

user1.history.add_records("user 1's log")
user1.history.print_records()
user2.history.add_records("user 2's log")
user2.history.print_records()
