#Rock Paper Scissors


from random import choice
from unicodedata import numeric
game = ["Rock", "Paper", "Scissor"]
chances = 0
us = 0
cs = 0

while True:

    rounds = input("Enter the number of rounds: ")

    count = rounds.isnumeric()
    if count == True:
        chances = int(rounds)

        for i in range(int(rounds)):
            computer = choice(game)
            user = input("Enter Rock, Paper, or Scissor: ")
            print("computer: ", computer)
            print("You: ", user)
            if (user in game):
                if computer == user:
                    print("Tie")

                elif computer == "Rock":
                    if user == "Paper":
                        print("You Won!")
                        us += 1
                    else:
                        print("Computer Won!")
                        cs += 1

                elif computer == "Paper":
                    if user == "Scissor":
                        print("You Won!")
                        us += 1
                    else:
                        print("Computer Won!")
                        cs += 1
                    
                else:
                    if user == "Rock":
                        print("You Won!")
                        us += 1
                    else:
                        print("Computer Won!")
                        cs += 1



            else:
                print("Invalid Input")
            chances -= 1 

            print("-----------------------------------------")
            print("User Score: ", us)
            print("Computer Score: ", cs)
            print("Chances remaining: ", chances)
            print("-----------------------------------------")



    if us > cs:
        print("You are the Winner!")
    elif cs > us:
        print("Computer is the Winner!")
    elif cs == us:
        print("Tie")
    play_again = input("Do you want to play again? Yes/No? ")

    if play_again == "Yes":
        continue
    elif play_again == "No":
        break
    else:
        print("Invalid")
        print("If you don't want to play, enter the number of rounds as 0")

    print("Thank You for Playing")


