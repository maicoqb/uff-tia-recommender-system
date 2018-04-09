import csv

from src.FileManager import FileManager

class FileManagerBuilder:

    filename = 'test_arquivo.csv'

    def __init__(self):
        self.users = 1
        self.items = 1

    def aFileManager(self):
        return FileManagerBuilder()
    
    def withUsers(self, amount):
        self.users = amount
        return self
    
    def withItems(self, amount):
        return self.withItemsList(range(0, amount))

    def withItemsList(self, list):
        self.items = list
        return self

    def __createFile(self):
        with open(self.filename, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            for _ in range(0, self.users):
                writer.writerow(self.items)

    def build(self):
        self.__createFile()
        return FileManager(self.filename)