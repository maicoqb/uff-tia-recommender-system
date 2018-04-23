import csv

class FileManager:
    
    def __init__(self, filename, header=None, delimiter=None):
        self.filename = filename
        self.header_idx = header
        self.header_row = []
        self.rows = []
        self.cols = []

        self.__readFile(delimiter)
    
    def __readFile(self, delimiter=None):
        with open(self.filename, newline='') as f:
            if delimiter != None:
                reader = csv.reader(f, delimiter=delimiter)
            else:
                reader = csv.reader(f)
            
            r = 0
            for row in reader:
                if self.header_idx != None and self.header_idx == r:
                    self.header_row = row
                else:
                    self.__addRow(row)
                    
                r = r+1
                
    def __addRow(self, row):
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
    
    def getColumns(self):
        return self.cols

    def getRows(self):
        return self.rows

    def setRows(self, rows):
        self.rows = []
        self.cols = []
        for row in rows:
            self.__addRow(row)
    
    def getHeader(self):
        return self.header_row if self.header_idx != None else self.getRow(1)