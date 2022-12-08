from random import randint
t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0, 2)]

player = False
while player == False:
    player = input("Choose wisely Rock, Paper, Scissors:")
    if player == computer:
        print("tie!!!")
    elif player == "Rock":
        if computer == "Paper":
            print("you lose ", computer, "covers  ", player)
        else:
            print("you win")
    elif player == "Paper":
        if computer == "Scissors":
            print("you lose")
        else:
            print("you win")
    elif player == "Scissors":
        if computer == "Rock":
            print("you lose")
        else:
            print("you win")
    else:
        print("That is not a valid play check your spellings")
    player = False
    computer = t[randint(0,2)]