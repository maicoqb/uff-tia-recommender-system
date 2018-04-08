
from .User import User
from .Item import Item

class RecommenderSystem:

    def __init__(self, fileManager):
        self.fileManager = fileManager
        pass
    
    def getUser(self, userN):
        return User()
    
    def getItem(self, itemN):
        return Item()
    
    def hasRating(self, userN, itemN):
        return True
    
    def getRating(self, userN, itemN):
        return 1
    
    def getUserBasedPrediction(self, userN, itemN):
        return 1
    
    def getItemBasedPrediction(self, userN, itemN):
        return 1
    