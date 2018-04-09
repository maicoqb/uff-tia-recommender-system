

class User:
    def __init__(self, reviews=1):
        self.reviews = reviews

    def getReviewsLength(self):
        return self.reviews