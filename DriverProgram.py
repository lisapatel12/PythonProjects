# Driver: Lisa Patel


# This program uses information from the other files in order to execute the trivia game.

import TriviaQuestions

def main():

    #Initializing variables
    counter = 0
    p1 = 0
    p2 = 0

    #For loop to go through all the questions
    for question in TriviaQuestions.triviaQuestions():
        
        #Player 1 
        if counter % 2 == 0:
            print('Question for the first player:')
            print(question.getQuestion())
            print('1.',question.getA1())
            print('2.',question.getA2())
            print('3.',question.getA3())
            print('4.',question.getA4())

            user = int(input('Enter your solution (a number between 1 and 4):'))
            #Makes sure to get a number between 1 to 4
            while not (user >= 1 and user <= 4):
                user = int(input('Enter your solution (a number between 1 and 4):'))
            
            #Check the user choice to see if its the correct answer
            if user == question.getCorrectAnswer():
                print('That is the correct answer.\n')
                p1 += 1
            else:
                print('That is incorrect. The correct answer is', question.getCorrectAnswer())
                print()

        #Player 2
        else:
            print('Question for the second player:')
            print(question.getQuestion())
            print('1.',question.getA1())
            print('2.',question.getA2())
            print('3.',question.getA3())
            print('4.',question.getA4())

            user = int(input('Enter your solution (a number between 1 and 4):'))
            #Makes sure to get a number between 1 to 4
            while not (user >= 1 and user <= 4):
                user = int(input('Enter your solution (a number between 1 and 4):'))

            #Check the user choice to see if its the correct answer
            if user == question.getCorrectAnswer():
                print('That is the correct answer.\n')
                p2 += 1
            else:
                print('That is incorrect. The correct answer is', question.getCorrectAnswer())
                print()

        counter += 1
    
    print('The first player earned', p1, 'points.')
    print('The second player earned', p2, 'points.')
    
    #To find out who scored higher and wins the game
    if(p1 > p2):
        print('The first player wins the game.')
    elif(p2 > p1):
        print('The second player wins the game.')
    elif(p1 == p2):
        print('It\'s a tie!')


#calling main() to run the program
main()
