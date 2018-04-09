
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
            user = self.getUser(userN)
            review = user.getReview(itemN)
        except Exception:
            return False

        return review != '?'
    
    def getRating(self, userN, itemN):
        return 1
    
    def getUserBasedPrediction(self, userN, itemN):
        return 1
    
    def getItemBasedPrediction(self, userN, itemN):
        return 1
    