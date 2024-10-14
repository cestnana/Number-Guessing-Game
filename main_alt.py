# Import necessary modules
from random import randint
from art import logo

# Global variables
target_number = randint(1, 100)  # Random number between 1 and 100
attempts = 0  # Tracks current attempt count
total_attempts = 10  # Default attempts (for easy mode)

# Display current status
def display_status(attempts_left):
  print(f"You have {attempts_left} attempts remaining to guess the number.")

# Game setup: display logo and determine difficulty
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a whole number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ")

# Adjust total attempts based on difficulty
total_attempts = 5 if difficulty == 'h' else 10

# Display the initial status
display_status(total_attempts)

# Main game loop
while attempts < total_attempts:
  # Get and validate user input
  while True:
    guess = input("Make a guess: ")
    if guess.isdigit():
      guess = int(guess)
      break
    print("Invalid input. Please enter a whole number.")

  attempts += 1  # Increment attempt count
  attempts_left = total_attempts - attempts  # Calculate attempts left

  # Check if the guess is correct
  if guess == target_number:
    print(f"You got it! The answer was {guess}.")
    break
  elif guess > target_number:
    print("Too high, guess again.")
  else:
    print("Too low, guess again.")

  display_status(attempts_left)  # Show remaining attempts

# If user runs out of attempts
if attempts >= total_attempts and guess != target_number:
  print(f"You've run out of guesses. The correct number was {target_number}. You lose.")