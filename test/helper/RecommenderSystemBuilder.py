
from .FileManagerBuilder import FileManagerBuilder
from src.RecommenderSystem import RecommenderSystem

class RecommenderSystemBuilder:

    def __init__(self):
        self.fmb = FileManagerBuilder().aFileManager()

    def aRecommenderSystem(self):
        return RecommenderSystemBuilder()

    def with3Users(self):
        self.fmb.withUsers(3)
        return self
    
    def with1ItemEach(self):
        self.fmb.withItems(1)
        return self
        
    def build(self):
        fileManager = self.fmb.build()
        return RecommenderSystem(fileManager)