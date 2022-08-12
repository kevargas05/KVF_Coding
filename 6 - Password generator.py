#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#
password_list = []
for x in range(1,nr_letters+1):
  final_letters = random.choice(letters)
  password_list += final_letters
#
for x in range(1,nr_symbols+1):
  final_simbols = random.choice(symbols)
  password_list += final_simbols
#
for x in range(1,nr_numbers+1):
  final_numbers = random.choice(numbers)
  password_list += final_numbers
#
# To shuffle the characthers in the list
random.shuffle(password_list)

# For loop to convert list into string
password = ""
for item in password_list:
  password += item
#
print(f"Your password is: {password}")
