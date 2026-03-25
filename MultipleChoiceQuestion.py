from HistoryGame import Question

class MultipleChoiceQuestion(Question):
    def __init__(self):
        super().__init()
        self.multipleChoiceQuestions = []
    
    def addQuestion(self, answer2, answer3): # wrong answers only
        
        self.multipleChoiceQuestions.append([self.question, self.answer, answer2, answer3])
        
    def getQuestions(self,):
        return self.multipleChoiceQuestions
        