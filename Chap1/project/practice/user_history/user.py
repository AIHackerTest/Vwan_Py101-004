from history import History
class User(object):

    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.history = History()
