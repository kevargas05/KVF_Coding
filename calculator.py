from calculator_art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(): # We use a function, in order to implement recursion. In case the user wants to start a new calculation
  print(logo)

  num1 = float(input("What's the first number?: ")) # We use a float in case the user tries float numbers
  for symbol in operations:
    print(symbol)
  should_continue = True
 #
  while should_continue: #  We use a while loop in case the user wants to continue calculating
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol] # Sets the variable to call the function inside the dictionary
    answer = calculation_function(num1, num2) # call the function inside the dictionary with the 2 parameters. And saves the return value into the variable
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  #
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator() # If the user wants to start a new calculation, recursion starts so all past values are cleared.
#
calculator()
