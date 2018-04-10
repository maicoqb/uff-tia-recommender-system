import csv

from src.FileManager import FileManager

class FileManagerBuilder:

    filename = 'test_arquivo.csv'
    
    def __init__(self):
        self.users = []
        self.items = []
        self.itemsN = []

    def aFileManager(self):
        return FileManagerBuilder()
    
    def withUsers(self, amount):
        self.users = [[] for _ in range(0, amount)]
        return self
    
    def withItems(self, amount):
        return self.withItemsList(range(0, amount))

    def withItemsList(self, itemList):
        self.items = itemList
        return self
    
    def withItemsListForUser(self, user, itemList):
        while user > len(self.users): self.users.append([])
        self.users[user-1] = itemList
        return self

    def __createFile(self):
        with open(self.filename, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            for items in self.users:
                if items == []:
                    items = self.items
                writer.writerow(items)

    def build(self):
        self.__createFile()
        return FileManager(self.filename)