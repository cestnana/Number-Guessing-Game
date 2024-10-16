# Import modules
from random import randint
from art import logo

# ----------------------
# Function declarations

def get_attempts_left(total, attempts_used):
  """Calculate and return remaining attempts."""
  return total - attempts_used

def display_status(attempt_left):
  """Display the current number of attempts left."""
  print(f"You have {attempt_left} attempts remaining to guess the number.")

def get_valid_guess():
  """Prompt the user for a valid guess (integer)."""
  while True:
    guess = input("Make a guess: ")
    try:
      return int(guess)
    except ValueError:
      print("Invalid input! Please enter a whole number (e.g., 51).")

def play_game():
  """Main game logic."""
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a whole number between 1 and 100.")
  
  # Set game difficulty
  game_mode = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ").lower()
  total_attempts = 5 if game_mode == 'h' else 10

  # Generate the target number
  target_number = randint(1, 100)
  
  # Start the guessing game
  for attempt_count in range(total_attempts):
    attempt_left = get_attempts_left(total_attempts, attempt_count)
    display_status(attempt_left)
    
    # Get the user's guess
    guess = get_valid_guess()
    
    # Check the guess
    if guess == target_number:
      print(f"You got it! The answer was {target_number}.")
      return  # End the game if guessed correctly
    elif guess > target_number:
      print("Too high. Try again!")
    else:
      print("Too low. Try again!")
  
  # If all attempts are used
  print("You've run out of guesses. You lose.")

# ----------------------
# Start the game
play_game()