
from .User import User
from .Item import Item

from .FileManager import FileManager
from .UserBasedPredictioneer import UserBasedPredictioneer

class RecommenderSystem:

    def __init__(self, fileManager):
        ':param FileManager fileManager'
        self.fileManager = fileManager
        self.userBasedPredictioneer = UserBasedPredictioneer(fileManager.getRows())
        pass
    
    def getUser(self, userN):
        userRow = self.fileManager.getRow(userN)
        return User(userRow)
    
    def getItem(self, itemN):
        itemColumn = self.fileManager.getColumn(itemN)
        return Item(len(itemColumn))
    
    def hasRating(self, userN, itemN):
        try:
            review = self.getRating(userN, itemN)
        except Exception:
            return False

        return review != '?'
    
    def getRating(self, userN, itemN):
        user = self.getUser(userN)
        return user.getReview(itemN)
    
    def getUserBasedPrediction(self, userN, itemN):
        return self.userBasedPredictioneer.getPrediction(userN, itemN)
    
    def getItemBasedPrediction(self, userN, itemN):
        return 1
    