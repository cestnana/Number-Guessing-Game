# import external module/file: 
import random
# import logo file
import art

# global variables:

# test print random integer: 

# print(target_number)
# for _ in range(10):
#   print(random.randint(1, 100))

# generate a random integer number between 1 to 100
target_number = random.randint(1, 100)

# initialize user guessing number
guess_number = 0

# initialize total attempts
total_attempts = 0

# initialize user attempts
attempt_count = 0

# set attempts left
attempt_left = 10

# initialize user first attempt
is_first_attempt = True

# initialize game mode 
game_mode = "not choose yet"

# flag/result of checking user input is number
is_number = True

# function declarations: 

# display current status
def current_status(): 
  print(f"You have {attempt_left} attempts remaining to guess the number.")
  
# Input Validation: 
def check_is_number(value):
  return isinstance(value, (int, float))

# main logic: 

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a whole number between 1 and 100.")
game_mode = input("Choose a difficulty. Type 'e' for easy or 'h' for 'hard': ")

# determine difficulty, 'easy mode' as default
if game_mode == "h":
  total_attempts = 5
else:
  total_attempts = 10
  
# set attempts left
attempt_left = total_attempts - attempt_count

# main game logic
# if attempt_left <= 0:
#   print("'result':, you lose.")
# else:
  
# display the target number for test
# print(f"The target number is: {target_number}")

while attempt_left > 0:
  # display the target number for test
  # print(f"The target number is: {target_number}")
  
  # check if user is not first guessing
  if not is_first_attempt:
    print("Guess again.")
  
  # display current status
  current_status()
  
  # check user input is number
  while True:
    # user_input = input("Please enter a number:")
    
    # get user's guessing number
    guess_number = (input("Make a guess: "))

    try:
      value = int(guess_number)
      print("The value you entered is:", value)
      break  # Input correctly will exit the loop
    except ValueError:
      # catch the error and handle it
      print("What you entered is not a whole number. Please re-enter it. (e.g. 51)")
        
  # # get user's guessing number
  # guess_number = int(input("Make a guess: "))
  # ! this may cause error when user input a really str
  # ! how to handle this ?
  
  # check user input is number
  # is_number = check_is_number(guess_number)
  
  # *input validation*
  # while is_number == False:
  #   print("Please type a number. (e.g. 50)")
  #   guess_number = input("Make a guess: ")
  #   is_number = check_is_number(guess_number)
  #   if is_number == True:
  #     break
  
  # user attempts + 1
  attempt_count += 1
  # update attempts left
  attempt_left = total_attempts - attempt_count
  
  if int(guess_number) == target_number: 
    current_status()
    print(f"You got it! The answer was {guess_number}.")
    break
  elif int(guess_number) > target_number:
    print("Too high.")
    is_first_attempt = False
  elif int(guess_number) < target_number:
    print("Too low.")
    is_first_attempt = False
  else: 
    print("Please input a valid number.")
    is_first_attempt = False
  
# after exit while loop is...
# the point user run out of attempts: 
if attempt_left <= 0 and guess_number != target_number:
  current_status()
  print("You've run out of guesses, you lose.")