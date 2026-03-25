import random # get random question, might remove this and put it in the main

class Question():
    # create private fields
    # list of questions, will be a 2d array containing list of mutiplechoice questions 
    # list of mutipleChoice, the correct answer will always be the first index
    # answer
    # question
    def __init__(self):
        self.questions = []
        self.answer = " "
        self.question = " "

    def setQuestion(self, question):
        self.question = question
    
    def setCorrectAnswer(self, answer):
        self.answer = answer

    def getQuestion(self, questionsList, questionNum):
        return questionsList[questionNum]

    def getCorrectAnswer(self):
        return self.answer

    def addQuestion(self):
        self.questions.append([self.question, self.answer])
        
    def getQuestions(self):
        return self.questions

    def checkAnswer(self, questionsList, questionNum):
        if questionsList[questionNum][1].casefold() == self.answer.casefold():
            return "correct"
        else:
            return "false"
        

