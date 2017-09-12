from user import User

class History(object):

    def __init__(self):
        self.records = ''
        self.user = User()

    def add_records(self,records):
        self.records = records

    def print_records(self):
        print(self.records)
