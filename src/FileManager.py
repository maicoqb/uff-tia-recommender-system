import csv

class FileManager:
    
    def __init__(self, filename):
        self.filename = filename
        self.rows = []
        self.cols = []

        self.__readFile()
    
    def __readFile(self):
        with open(self.filename, newline='') as f:
            reader = csv.reader(f)
            
            for row in reader:
                self.rows.append(row)
                
                for idx, col in enumerate(row):
                    while idx >= len(self.cols):
                        self.cols.append([])

                    temp_col = self.cols[idx]
                    temp_col.append(col)
                    self.cols[idx] = temp_col

    def getColumn(self, columnN):
        return self.cols[columnN-1]

    def getRow(self, rowN):
        return self.rows[rowN-1]
    
    def getRows(self):
        return self.rows
            
