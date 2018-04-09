import csv

from src.FileManager import FileManager

class FileManagerBuilder:

    filename = 'test_arquivo.csv'
    users = 1
    items = []
    itemsN = []

    def aFileManager(self):
        return FileManagerBuilder()
    
    def withUsers(self, amount):
        self.users = amount
        return self
    
    def withItems(self, amount):
        return self.withItemsList(range(0, amount))

    def withItemsList(self, itemList):
        self.items = itemList
        return self
    
    def withItemsListForN(self, n, itemList):
        while n >= len(self.itemsN): self.itemsN.append([])
        self.itemsN[n] = itemList
        return self

    def __createFile(self):
        with open(self.filename, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            for i in range(0, self.users):
                items = self.items
                if self.itemsN != [] and self.itemsN[i] != []:
                    items = self.itemsN[i]

                writer.writerow(items)

    def build(self):
        self.__createFile()
        return FileManager(self.filename)