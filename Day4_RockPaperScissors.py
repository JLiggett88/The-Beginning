import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK'''
# Paper
paper = '''     
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
PAPER'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS'''


def play_game():
    your_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors "))
    if your_choice == 0:
        print(rock)
    elif your_choice == 1:
        print(paper)
    elif your_choice == 2:
        print(scissors)
    else:
        print("Wrong Input")

    print("Computer chose:")

    com_choices = [0, 1, 2]
    com_pick = random.choice(com_choices)

    if com_pick == 0:
        print(rock)
    elif com_pick == 1:
        print(paper)
    elif com_pick == 2:
        print(scissors)

    if your_choice == 0 and com_pick == 0:
        print("YOU TIE!")
    elif your_choice == 0 and com_pick == 1:
        print("YOU LOSE!")
    elif your_choice == 0 and com_pick == 2:
        print("YOU WIN!")
    elif your_choice == 1 and com_pick == 0:
        print("YOU WIN")
    elif your_choice == 1 and com_pick == 1:
        print("YOU TIE!")
    elif your_choice == 1 and com_pick == 2:
        print("YOU LOSE!")
    elif your_choice == 2 and com_pick == 0:
        print("YOU LOSE!")
    elif your_choice == 2 and com_pick == 1:
        print("YOU WIN!")
    elif your_choice == 2 and com_pick == 2:
        print("YOU TIE!")
    else:
        print("Invalid")

    play_again = input("PLAY AGAIN? Y or N?  ").lower()

    if play_again == "y":
        play_game()
    else:
        print("Good-Bye")


play_game()
