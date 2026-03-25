class Player:
    def __init__(self):
        self.highScore = 0
        self.name = " "

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setHighScore(self, score):
        self.highScore = score
    
    def getHighScore(self):
        return self.highScore