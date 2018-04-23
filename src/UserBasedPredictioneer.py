
import src.library as pearson

class UserBasedPredictioneer:

    def __init__(self, rows):
        self.rows = self.__clearRows(rows)
        self.__rowsSize = len(rows)
        self.__colsSize = len(rows[0])

    def getPrediction(self, n, m):
        filteredRows = self.getFilteredRows(m)
        userRow = filteredRows[n-1]

        ma = pearson.mean(userRow)
        simDevSum = 0
        simSum = 0

        for b, row in enumerate(filteredRows):
            if n-1 == b or row == None:
                continue
            else:
                if self.rows[b][m-1] == '?': continue
                similarity = pearson.pearsonCorrelation(userRow, row)
                devb = (self.rows[b][m-1] - pearson.mean(self.__filter(self.rows[b])))
                simDevSum += (similarity * devb)
                simSum += similarity

        simDevDiff = 0 if simSum == 0 else (simDevSum / simSum)

        return (ma + simDevDiff)

    def __filter(self, row):
        _row = []
        for i in row:
            if i == '?': continue
            _row.append(i)
        return _row

    def getFilteredRows(self, m):
        
        filteredRows = []
        idxToRemove = []

        for row in self.rows:
            _row = []
            for index, item in enumerate(row):
                if m-1 == index:
                    continue
                else:
                    if item == '?': idxToRemove.append(len(_row))
                    _row.append(item)
            filteredRows.append(_row)
        
        for idx in idxToRemove:
            for r, row in enumerate(filteredRows):
                _row = []
                for i, item in enumerate(row):
                    if i == idx or item == '?': continue
                    _row.append(item)
                if len(_row) == 0: 
                    _row = None
                filteredRows[r] = _row

        return filteredRows

    def __clearRows(self, rows):
        for i, row in enumerate(rows):
            for j, v in enumerate(row):
                if v == '?': continue
                else: row[j] = int(v)
            rows[i] = row
            
        return rows