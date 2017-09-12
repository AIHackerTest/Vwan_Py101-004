
class History(object):
    id = 1

    def __init__(self):
        self.records = {}

    def add_records(self,records):
        self.records[self.id] = records
        self.id += 1

    def show_records(self):
        if (len(self.records) == 0):
            print ("Not history records are found, please do some search and retry")
        else:
            for k,v in self.records.items():
                print(f"{k} {v}")
