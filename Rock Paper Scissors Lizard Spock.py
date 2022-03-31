#Lisa Patel (Driver)(U50140470) Adit Prabhu (Navigator)(U72452636)
#import random
import random
#list out the choices
L=['rock','paper','scissors','lizard','spock']
#print starting message
print("Lets play Rock, Paper, Scissors, Lizard, Spock!")
#define counts
user_counter=0
computer_counter=0
tie_counter=0
total_counter=0
# create loop that breaks when no is stated
while True:
    user=input("Enter your choices:")
    while True:
        #check if the choices are from the List L, if not input invalid print
        if user.lower() not in L:
            user = input("That's invalid. Please enter Rock, Paper, Scissors, Lizard or Spock:")
        else:
            break
    #make computer create a random choice
    computer=random.choice(L)
    print("Computer choose",computer)
    #create all possibilties for the user to win
    if user.lower()=="scissors" and computer=="paper":
        print("Scissors cuts Paper! Human wins!")
        user_counter += 1
    elif user.lower()=="paper" and computer=="rock":
        print("Paper covers Rock! Human wins!")
        user_counter += 1
    elif user.lower()=="rock" and computer=="lizard":
        print("Rock crushes Lizard! Human wins!")
        user_counter += 1
    elif user.lower()=="lizard" and computer=="spock":
        print("Lizard poisons Spock! Human wins!")
        user_counter += 1
    elif user.lower()=="spock" and computer=="scissors":
        print("Spock smashes Scissors! Human wins!")
        user_counter += 1
    elif user.lower()=="lizard" and computer=="paper":
        print("Lizard eats Paper! Human wins!")
        user_counter += 1
    elif user.lower()=="paper" and computer=="spock":
        print("Paper disproves Spock! Human wins!")
        user_counter += 1
    elif user.lower()=="spock" and computer=="rock":
        print("Spock vaporizes Rock! Human wins!")
        user_counter += 1
    elif user.lower()=="rock" and computer=="scissors":
        print("Rock crushes Scissors! Human wins!")
        user_counter += 1
    #create all possibilites for the computer to win
    elif computer=="scissors" and user.lower()=="paper":
        print("Scissor cuts Paper! Computer wins!")
        computer_counter += 1
    elif computer=="paper" and user.lower()=="rock":
        print("Paper covers Rock! Computer wins!")
        computer_counter += 1
    elif computer=="rock" and user.lower()=="lizard":
        print("Rock crushes Lizard! Computer wins!")
        computer_counter += 1
    elif computer=="lizard" and user.lower()=="spock":
        print("Lizard poisons Spock! Computer wins!")
        computer_counter += 1
    elif computer=="spock" and user.lower()=="scissors":
        print("Spock smashes Scissor! Computer wins!")
        computer_counter += 1
    elif computer=="scissors" and user.lower()=="lizard":
        print("Scissor decapitates Lizard! Computer wins!")
        computer_counter += 1
    elif computer=="lizard" and user.lower()=="paper":
        print("Lizard eats Paper! Computer wins!")
        computer_counter += 1
    elif computer=="paper" and user.lower()=="spock":
        print("Paper disproves Spock! Computer wins!")
        computer_counter += 1
    elif computer=="spock" and user.lower()=="rock":
        print("Spock vaporizes Rock! Computer wins!")
        computer_counter += 1
    elif computer=="rock" and user.lower()=="scissors":
        print("Rock crushes Scissors! Computer wins!")
        computer_counter += 1
    #If none of these conditiosn work, its a tie
    else:
        print("Its a Tie")
        tie_counter += 1
    total_counter += 1
    flag=0
    #create input to play game again
    choice=input("Play again? (yes/no):")
    #check if it is a valid input
    while True:
        if choice.lower()=='yes':
            break
        elif choice.lower()=='no':
            flag=1
            break
    #print message for invalid response and to get a valid response
        else:
            choice= input("Invalid response. Play again? Enter yes or no only:")
    if flag== 1:
        break
        print()
#print stats of the games played
print()
print("Number of games played:",total_counter)
print("Games you won:",user_counter)
print("Games the computer won:", computer_counter)
print("Tie games:",tie_counter)
print("Thanks for playing!")

    
    
