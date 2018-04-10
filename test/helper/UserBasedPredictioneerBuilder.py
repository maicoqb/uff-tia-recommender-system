
from src.UserBasedPredictioneer import UserBasedPredictioneer

class UserBasedPredictioneerBuilder():

    def __init__(self):
        self.rows = []

    def aUserBasedPredictioneer(self):
        return UserBasedPredictioneerBuilder()
    
    def with5Users(self):
        self.rows = [[] for _ in range(0,5)]
        return self
    
    def with5Items(self):
        self.rows = [[1 for _ in range(0,5)] for user in self.rows]
        return self
    
    def theUserNWithRatings(self, n, list):
        self.rows[n-1] = list
        return self

    def theUsersInRangeWithRatings(self, range, list):
        for n in range: self.theUserNWithRatings(n, list)
        return self
    
    def build(self):
        return UserBasedPredictioneer(self.rows)

    def withRattingNWithValue(self, n, value):
        return self.aUserBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .theUserNWithRatings(1, [value for _ in range(0,n-1)] + ['?']) \
                .theUsersInRangeWithRatings(range(2,n),[value for _ in range(0,n)])
    
    def withRattingInMiddleWithValue(self, value):
        nRatting = [value for _ in range(0,2)] + ['?'] + [value for _ in range(3,5)]
        return self.aUserBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .theUsersInRangeWithRatings(range(1,2),[value for _ in range(0,5)]) \
                .theUserNWithRatings(3, nRatting) \
                .theUsersInRangeWithRatings(range(4,5),[value for _ in range(0,5)])
    
    def withRattingIn3And4(self, value):
        nRatting = [value for _ in range(0,2)] + ['?'] + ['?'] + [value]
        oRatting = [value for _ in range(0,5)]
        return self.aUserBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .theUserNWithRatings(1, nRatting) \
                .theUsersInRangeWithRatings(range(2,6), oRatting)
    