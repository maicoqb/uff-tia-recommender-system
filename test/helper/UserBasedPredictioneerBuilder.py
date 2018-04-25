
from src.UserBasedPredictioneer import UserBasedPredictioneer

class UserBasedPredictioneerBuilder():

    def __init__(self):
        self.rows = []

    def aUserBasedPredictioneer(self):
        return UserBasedPredictioneerBuilder()
    
    def withAnyData(self):
        return self.with5Items().with5Users()

    def with5Users(self):
        self.rows = [[] for _ in range(0,5)]
        return self
    
    def with5Items(self):
        self.rows = [[1 for _ in range(0,5)] for user in self.rows]
        return self
    
    def withRatings(self, list):
        self.rows = list
        return self

    def theUserNWithRatings(self, n, list):
        self.rows[n-1] = list
        return self

    def theUsersInRangeWithRatings(self, range, list):
        for n in range: self.theUserNWithRatings(n, list)
        return self
    
    def build(self):
        return UserBasedPredictioneer(self.rows)
    
    def withRatingNWithValue(self, n, value):
        return self.aUserBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .theUserNWithRatings(1, [value for _ in range(0,n-1)] + ['?']) \
                .theUsersInRangeWithRatings(range(2,n),[value for _ in range(0,n)])
    
    def withRatingInMiddleWithValue(self, value):
        nRating = [value for _ in range(0,2)] + ['?'] + [value for _ in range(3,5)]
        return self.aUserBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .theUsersInRangeWithRatings(range(1,2),[value for _ in range(0,5)]) \
                .theUserNWithRatings(3, nRating) \
                .theUsersInRangeWithRatings(range(4,5),[value for _ in range(0,5)])
    
    def withRatingIn3And4(self, value):
        nRating = [value for _ in range(0,2)] + ['?'] + ['?'] + [value]
        oRating = [value for _ in range(0,5)]
        return self.aUserBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .theUserNWithRatings(1, nRating) \
                .theUsersInRangeWithRatings(range(2,6), oRating)
        
    def withDefaultDataSet(self):
        return self.withRatings([
                        [2,3,3,3,4,5,3,'?',4,5],
                        [3,3,5,5,5,3,5,1,'?',4],
                        [1,2,2,3,4,3,3,2,5,'?'],
                        [3,3,2,2,4,3,'?',4,1,1],
                        [5,4,4,3,3,3,4,5,'?',3],
                        [3,4,2,3,3,'?',2,5,4,3],
                        [2,3,4,4,3,4,3,5,'?',3],
                        [1,2,2,5,3,4,5,3,3,'?'],
                        [1,5,3,5,3,4,'?',5,4,3],
                        [4,4,4,3,2,3,5,2,3,'?'],
                        [2,3,5,3,3,5,5,1,5,'?'],
                        [3,4,3,5,4,5,5,4,2,3],
                        [4,2,2,5,3,3,'?',3,5,3],
                        [5,5,1,1,5,1,5,4,3,5],
                        [3,3,2,1,4,'?',5,5,2,4],
                        [5,3,5,'?',4,4,4,3,2,3],
                        [3,2,3,1,3,4,'?',3,3,1],
                        ['?',4,5,3,4,2,1,4,4,4],
                        [1,3,3,2,4,3,2,'?',3,4],
                        [4,2,3,2,'?',3,2,3,2,1],
                        [3,5,4,3,3,4,4,'?',3,3],
                        [3,'?',2,1,4,3,3,4,2,3],
                        [2,1,2,3,4,1,'?',2,4,1],
                        [5,4,4,'?',3,4,5,3,4,2],
                        [3,4,3,5,'?',2,1,4,5,3],
                        [5,4,3,2,3,4,4,'?',3,1],
                        [3,'?',5,4,4,5,3,3,3,2],
                        [3,4,4,2,'?',5,3,4,5,3],
                        [2,3,4,'?',3,1,2,3,4,3],
                        [5,3,2,4,4,5,3,3,'?',4]
                ])
    