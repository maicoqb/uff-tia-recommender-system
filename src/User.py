

class User:
    def __init__(self, reviews=[]):
        self.reviews = reviews

    def getReviewsLength(self):
        return len(self.reviews)
    
    def getReview(self, idx):
        return self.reviews[idx-1]