
from .FileManagerBuilder import FileManagerBuilder
from src.RecommenderSystem import RecommenderSystem

class RecommenderSystemBuilder:

    def __init__(self):
        self.fmb = FileManagerBuilder().aFileManager()

    def aRecommenderSystem(self):
        return RecommenderSystemBuilder()

    def withRatings(self, ratings):
        for idx, items in enumerate(ratings):
            self.fmb.withItemsListForUser(idx+1, items)
        return self

    def with1User(self):
        self.fmb.withUsers(1)
        return self

    def with3Users(self):
        self.fmb.withUsers(3)
        return self
    
    def with5Users(self):
        self.fmb.withUsers(5)
        return self

    def with1Item(self, rating=1):
        self.fmb.withItemsList([rating])
        return self
    
    def with1ItemEach(self):
        self.fmb.withItems(1)
        return self

    def with3ItemsEach(self):
        self.fmb.withItems(3)
        return self
    
    def withOnlyItem1And3(self):
        self.fmb.withItemsList([1, '?', 1])
        return self
    
    def with5ItemsNM(self):
        itemListNM = lambda n: [n*m for m in [1,2,3,4,5]]
        return self.withRatings([
            itemListNM(1),
            itemListNM(2),
            itemListNM(3),
            itemListNM(4),
            itemListNM(5)
        ])
    
    def build(self):
        fileManager = self.fmb.build()
        return RecommenderSystem(fileManager)