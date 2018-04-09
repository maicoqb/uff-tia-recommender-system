
from .User import User
from .Item import Item

from .FileManager import FileManager

class RecommenderSystem:

    def __init__(self, fileManager):
        """
        :param FileManager fileManager: 
        """
        self.fileManager = fileManager
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
        return 1
    
    def getItemBasedPrediction(self, userN, itemN):
        return 1
    