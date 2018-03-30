import csv

class FileManager:
    
    def __init__(self, filename):
        self.filename = filename
        self.users = []
        self.items = []

        self.__readFile(filename)
    
    def __readFile(self, filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            
            for row in reader:
                self.users.append('')
                
                if not len(self.items):
                    for i in range(0, len(row)):
                        self.items.append('')


    def getUsers(self):
        return self.users
        
    def getItems(self):
        return self.items
        
            
