# import external module/file: 
from random import randint
# import logo from module/file:
from art import logo

# ------------------
# global variables:

# generate a random integer number between 1 to 100
target_number = randint(1, 100)

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

# ----------------------
# function declarations: 

# display current status
def current_status(): 
  print(f"You have {attempt_left}/{total_attempts} attempts remaining to guess the number.")
  
# display initial status
def initial_status(): 
  print(f"You have {total_attempts} attempts to guess the number.")
  

# -----------
# main logic: 

print(logo)
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

# display the initial status
initial_status()

# if user still has attempts left
while attempt_left > 0:  
  # get user input and validate it
  while True:
    # get user's guessing number
    guess_number = (input("Make a guess: "))
    # check user input is number
    try:
      value = int(guess_number)
      # print("The value you entered is:", value)
      break  # Input correctly will exit the loop
    except ValueError:
      # catch the error and handle it
      print("What you entered is not a whole number. Please re-enter it. (e.g. 51)")
        
  # user attempts + 1
  attempt_count += 1
  # update attempts left
  attempt_left = total_attempts - attempt_count
  # determine the guessing result
  if int(guess_number) == target_number: 
    print(f"You got it! The answer was {guess_number}.")
    current_status()
    break
  elif int(guess_number) > target_number:
    print("Too high, guess again.")
    current_status()
    is_first_attempt = False
  elif int(guess_number) < target_number:
    print("Too low, guess again.")
    current_status()
    is_first_attempt = False
  else: 
    print("Please input a valid number.")
    current_status()
    is_first_attempt = False
  
# after exit while loop is...
# the point user run out of attempts: 
if attempt_left <= 0 and guess_number != target_number:
  print("You've run out of guesses, you lose.")