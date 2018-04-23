import math
import src.library as pearson


class ItemBasedPredictioneer:

    def __init__(self, rows):
        self.rows = self.__clearRows(rows)
        self.__rowsSize = len(rows)
        self.__colsSize = len(rows[0])

    def __getItem(self, user, item):
        _item = []
        for r, row in enumerate(self.rows):
            if r == user-1: continue
            for i, v in enumerate(row):
                if i == item-1: _item.append(v)
        return _item

    def getPrediction(self, n, m):
        itemCol = self.__getItem(n, m)
        userRow = self.rows[n-1]

        similarities = [None for _ in range(0, self.__colsSize)]
        for i in range(0, self.__colsSize):
            if i == n-1:
                continue
            item = self.__getItem(n, i+1)
            similarities[i] = self.__calculateSimilarity(itemCol, item)

        sumSimR = 0
        sumSim = 0
        for i, r in enumerate(userRow):
            if i == m-1: continue
            for sim in similarities:
                if sim == None or r == '?': continue
                sumSimR += (sim * r)
                sumSim += sim

        if sumSim == 0: return 0
        return sumSimR / sumSim

    def __calculateSimilarity(self, itemCol, item):
        sumVec = 0
        modVecA = 0
        modVecB = 0
        
        for idx, a in enumerate(itemCol):
            b = item[idx]
            if a == '?' or b == '?': continue

            a = int(a)
            a = int(b)
            sumVec += a * b
            modVecA += pow(a, 2)
            modVecB += pow(b, 2)
        
        modVecA = math.sqrt(modVecA)
        modVecB = math.sqrt(modVecB)

        if modVecA == 0 or modVecB == 0:
            return 0
        
        return sumVec / (modVecA * modVecB)

    def __clearRows(self, rows):
        for i, row in enumerate(rows):
            for j, v in enumerate(row):
                if v == '?':
                    continue
                else:
                    row[j] = int(v)
            rows[i] = row

        return rows
