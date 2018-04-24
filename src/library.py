import math
import csv
from collections import UserList

from src.FileManager import FileManager

def mean(A):
    m = 0
    for n in A: m += int(n)
    return (1 / len(A)) * m

def covariance(X, Y):
    mx = mean(X)
    my = mean(Y)

    C = 0
    for i, x in enumerate(X):
        y = int(Y[i])
        x = int(x)
        C += (x - mx)*(y - my)

    return C

def standardDeviation(A):
    ma = mean(A)

    sd = 0
    for a in A:
        a = int(a)
        sd += math.pow(a - ma, 2)

    return sd

def pearsonCorrelation(X, Y):
    a = covariance(X, Y)
    b = math.sqrt(standardDeviation(X) * standardDeviation(Y))

    if b == 0: return 0
    return a / b

def pearsonrFake(X, Y):
    return [pearsonCorrelation(X,Y)]

class npFake:

    @staticmethod
    def delete(arr, idx):
        newArr = []
        for (i, v) in enumerate(arr):
            if(i!=idx): newArr.append(v)
        return npFake.array(newArr)
    
    @staticmethod
    def mean(arr):
        return mean(arr)
    
    @staticmethod
    def array(arr):
        return npFakeArrayAcessor(arr)

class npFakeArrayAcessor(UserList):

    def __init__(self, initlist):
        super().__init__(initlist)
        self.values = self
    
    def __add__(self, other):
        if isinstance(other, int):
            new_data = []
            for val in self.data:
                new_data.append(val + other)
                
            return self.__class__(list(new_data))
        return super().__add__(other)

    __radd__ = __add__

    def astype(self, _type):
        new_data = []
        for val in self.data:
            new_data.append(_type(val))

        return self.__class__(list(new_data))
    
class pdFake:

    @staticmethod
    def read_csv(filename, header=0, sep=';'):
        fileManager = FileManager(filename, header, sep)
        return pdFakeFile(fileManager)

class pdFakeFile:

    def __init__(self, fileManager):
        self.__updateFileManager(fileManager)
    
    def drop(self, label, axis=1):
        rows = self.fileManager.getRows()
        firstRow = self.fileManager.getHeader()
        _rows = []

        indexToRemove = None

        for (idx, value) in enumerate(firstRow):
            if value == label:
                indexToRemove = idx
        
        for row in rows:
            _row = npFake.delete(row, indexToRemove)
            _rows.append(_row)
        
        self.fileManager.setRows(_rows)
        self.__updateFileManager(self.fileManager)

        return self
    
    def getRows(self):
        return self.fileManager.getRows()

    def getColumns(self):
        return self.fileManager.getColumns()

    def __updateFileManager(self, fileManager):
        self.fileManager = fileManager
        self.iloc = pdFakeIlocAcessor(self.fileManager)
        self.index = range(0, len(self.fileManager.getRows()))

class pdFakeIlocAcessor:

    def __init__(self, fileManager):
        self.fileManager = fileManager

    def __getitem__(self,key):
        arr = []
        if isinstance(key, int):
            arr = self.fileManager.getRow(key+1)
        elif isinstance(key[1], int):
            arr = self.fileManager.getColumn(key[1]+1)
        return npFake.array(arr)


    

        
            


