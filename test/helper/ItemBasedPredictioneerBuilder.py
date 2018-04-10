
from src.ItemBasedPredictioneer import ItemBasedPredictioneer

class ItemBasedPredictioneerBuilder():

    def __init__(self):
        self.rows = []

    def aItemBasedPredictioneer(self):
        return ItemBasedPredictioneerBuilder()
    
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

    def withRatings(self, list):
        self.rows = list
        return self

    def with5x5RatingsWithoutValuesIn(self, withouts, value):
        ratings = []

        for i in range(0,5):
            rating = []
            for j in range(0,5):
                without = False
                for w in withouts: 
                    if [i+1,j+1] == w: without = True
                if without: rating.append('?')
                else: rating.append(value)
            ratings.append(rating)
                

        return self.aItemBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .withRatings(ratings)


    def with5x5RatingValue(self, value):
        return self.aItemBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .theUserNWithRatings(1, [value for _ in range(0,4)] + ['?']) \
                .theUsersInRangeWithRatings(range(2,5),[value for _ in range(0,5)])
    
    def with5x5RatingInMiddle(self, value):
        nRating = [value for _ in range(0,2)] + ['?'] + [value for _ in range(3,5)]
        return self.aItemBasedPredictioneer() \
                .with5Users() \
                .with5Items() \
                .theUsersInRangeWithRatings(range(1,2),[value for _ in range(0,5)]) \
                .theUserNWithRatings(3, nRating) \
                .theUsersInRangeWithRatings(range(4,5),[value for _ in range(0,5)])
    
    def build(self):
        return ItemBasedPredictioneer(self.rows)
