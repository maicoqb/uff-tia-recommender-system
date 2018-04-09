

class User:
    def __init__(self, reviews=[]):
        self.reviews = reviews

    def getReviewsLength(self):
        return len(self.reviews)
    
    def getReview(self, idx):
        review = self.reviews[idx-1]
        return review if review == '?' else int(review)