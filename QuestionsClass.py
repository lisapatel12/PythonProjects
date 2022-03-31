# Driver:Lisa Patel

# This program defines the Questions class for the other files

class Questions:
    #Constructor method
    def __init__(self, question, a1, a2, a3, a4, correct_answer):
        self.question = question
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3 
        self.a4 = a4
        self.correct_answer = correct_answer

    #Setter methods
    def setQuestion(self, question):
        self.question = question

    def setA1(self,a1):
        self.a1 = a1
    
    def setA2(self, a2):
        self.a2 = a2

    def setA3(self, a3):
        self.a3 = a3
    
    def setA4(self, a4):
        self.a4 = a4

    def setCorrectAnswer(self, correct_answer):
        self.correct_answer = correct_answer

    #Getter methods
    def getQuestion(self):
        return self.question

    def getA1(self):
        return self.a1

    def getA2(self):
        return self.a2

    def getA3(self):
        return self.a3

    def getA4(self):
        return self.a4

    def getCorrectAnswer(self):
        return self.correct_answer

    
