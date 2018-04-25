from collections import namedtuple
import src.library as library

class UserBasedPredictioneer:

    def __init__(self, rows):
        self.rows = self.__clearRows(rows)
        self.__rowsSize = len(rows)
        self.__colsSize = len(rows[0])

    def getPrediction(self, n, m):
        userRow = self.rows[n-1]
        othersUsers = self.getUsersWhoHaveThisItem(m)

        othersUsers = library.ArrayFunctions.delete(othersUsers, n-1)

        simDevSum = 0
        simSum = 0

        for row in othersUsers:
            filteredRows = self.filterSideBySide(userRow, row)
            similarity = library.pearsonCorrelation(filteredRows.first, filteredRows.second)
            if(similarity > float(0.4)):
                devb = (row[m-1] - library.mean(self.filter(row)))
                simDevSum += (similarity * devb)
                simSum += similarity

        simDevDiff = 0 if simSum == 0 else (simDevSum / simSum)

        ma = library.mean(self.filter(userRow))
        return (ma + simDevDiff)

    def filter(self, row):
        return [r for r in row if r != '?']
    
    def filterSideBySide(self, first, second):
        FilteredRows = namedtuple('FilteredRows', ['first', 'second'])
        filteredRows = FilteredRows(first=[], second=[])
        
        for (idx, fval) in enumerate(first):
            sval = second[idx]
            if '?' != fval and '?' != sval:
                filteredRows.first.append(fval)
                filteredRows.second.append(sval)

        return filteredRows

    def getUsersWhoHaveThisItem(self, m):
        return [row for row in self.rows if row[m-1] != '?']

    def __clearRows(self, rows):
        for i, row in enumerate(rows):
            for j, v in enumerate(row):
                if v == '?': continue
                else: row[j] = int(v)
            rows[i] = row
            
        return rows