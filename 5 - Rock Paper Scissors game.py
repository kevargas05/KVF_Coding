rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#
import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
#
if player_choice > 2:
  print("Wrong number, try again.")
else:
    #
    options= [rock, paper, scissors]
    print(options[player_choice])
    print("Computer chose:\n")
    print(options[computer_choice])
    #
    if player_choice == 0:
      if computer_choice == 0:
        print("Draw!")
      elif computer_choice == 1:
        print("You Lose!")
      elif computer_choice == 2:
        print("You Won!!!!!!")
    #
    if player_choice == 1:
      if computer_choice == 1:
        print("Draw!")
      elif computer_choice == 0:
        print("You Won!!!!!!")
      elif computer_choice == 2:
        print("You Lose!")
    #
    if player_choice == 2:
      if computer_choice == 2:
        print("Draw!")
      elif computer_choice == 1:
        print("You Won!!!!!!")
      elif computer_choice == 0:
        print("You Lose!")

