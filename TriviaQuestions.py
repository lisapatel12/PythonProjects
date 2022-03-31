# Driver: Luis Vega (U19971280)
# Navigator: Lisa Patel (U50140470)

# This program defines a function that creates a list of trivia question objects and returns it as a list.

import QuestionsClass

def triviaQuestions():

    q1 = QuestionsClass.Questions('How many days are in a lunar year?','354','365','243','379', 1)
    q2 = QuestionsClass.Questions('What is the largest planet?','Mars','Jupiter','Earth','Pluto', 2)
    q3 = QuestionsClass.Questions('What is the largest kind of whale?','Orca whale','Humpback whale','Beluga whale','Blue whale', 4)
    q4 = QuestionsClass.Questions('Which dinosaur could fly?','Triceratops','Tyrannosaurus Rex','Pteranodon','Diplodocus', 3)
    q5 = QuestionsClass.Questions('Which of these Winnie the Pooh characters is a donkey?','Pooh','Eeyore','Piglet','Kanga', 2)
    q6 = QuestionsClass.Questions('What is the hottest planet?','Mars','Pluto','Earth','Venus', 4)
    q7 = QuestionsClass.Questions('Which dinosaur had the largest brain compared to body size?','Troodon','Stegosaurus','Ichthyosaurus','Gigantoraptor', 1)
    q8 = QuestionsClass.Questions('What is the largest type of penguins?','Chinstrap penguins','Macaroni penguins','Emperor penguins','White-flippered penguins', 3)
    q9 = QuestionsClass.Questions('Which children\'s story character is a monkey?','Winnie the Pooh','Curious George','Horton','Goofy', 2)
    q10 = QuestionsClass.Questions('How long is a year on Mars?','550 Earth days','498 Earth days','126 Earth days','687 Earth days', 4)

    
    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    
    return questions
