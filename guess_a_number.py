from random import randint
logo = """   ____     _   _ U _____ u ____    ____           ____      _      __  __  U _____ u 
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u     U /"___|uU  /"\  uU|' \/ '|u\| ___"|/ 
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/      \| |  _ / \/ _ \/ \| |\/| |/ |  _|"   
 | |_| |   | |_| | | |___  u___) | u___) |       | |_| |  / ___ \  | |  | |  | |___   
  \____|  <<\___/  |_____| |____/>>|____/>>       \____| /_/   \_\ |_|  |_|  |_____|  
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)      _)(|_   \\    >><<,-,,-.   <<   >>  
 (__)__)     (__) (__) (__)(__)    (__)          (__)__) (__)  (__)(./  \.) (__) (__) 
"""
print(logo)
answer = randint(1, 100)
#
def guess_check(user_guess):
  '''
  Receives user guess and compares it against the random answer.
  It returns:
    If guess > answer: 2
    If guess < answer: 1
    If guess == answer: 0
  '''
  if user_guess > answer:
    print("Too High\n")
    result = 2
  elif user_guess < answer:
    print("Too Low\n")
    result = 1
  else:
    print(f"You got it! The answer was {answer}")  
    result = 0
  return result
#
def turns_remaining(selected_dificulty):
  '''
  Receives a dificulty and return the number of turns remaining
  It returns:
    If easy: 10
    If hard: 5
  '''
  if selected_dificulty == "easy":
    return 10
  elif selected_dificulty == "hard":
    return 5
#
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
dificulty= input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
turns = turns_remaining(dificulty)
guess = int(input("Make a guess:\n"))
#
x = guess_check(guess)
while x != 0:
  turns -= 1 
  if turns == 0:
    print("You've run out of guesses, you lose.")
    x = 0
  else:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess:\n"))
    x = guess_check(guess)
