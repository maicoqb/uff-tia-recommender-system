import csv

from src.FileManager import FileManager

class FileManagerBuilder:

    filename = 'test_arquivo.csv'
    
    def __init__(self):
        self.rows = []
        self.columns = []
        self.columnsN = []

    def withUsers(self, amount):
        self.rows = [[] for _ in range(0, amount)]
        return self
    
    def withItems(self, amount):
        return self.withItemsList(range(0, amount))

    def withItemsList(self, itemList):
        self.columns = itemList
        return self
    
    def withItemsListForUser(self, user, itemList):
        while user > len(self.rows): self.rows.append([])
        self.rows[user-1] = itemList
        return self

    @staticmethod
    def aFileManager():
        return FileManagerBuilder()
    
    @staticmethod
    def fromList(list):
        fmb = FileManagerBuilder.aFileManager()
        for (idx, row) in enumerate(list):
            fmb.withItemsListForUser(idx+1, row)
        return fmb

    def __createFile(self):
        with open(self.filename, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            for columns in self.rows:
                if columns == []:
                    columns = self.columns
                writer.writerow(columns)

    def build(self):
        self.__createFile()
        return FileManager(self.filename)