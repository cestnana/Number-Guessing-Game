# test print random integer: 
# print(target_number)
# for _ in range(10):
#   print(random.randint(1, 100))

# main game logic
# if attempt_left <= 0:
#   print("'result':, you lose.")
# else:
  
# display the target number for test
# print(f"The target number is: {target_number}")

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
  
  # display the target number for test
  # print(f"The target number is: {target_number}")

  # check if user is not first guessing
  # if not is_first_attempt:
  #   print("Guess again.")
  
  # display current status
  # current_status()
  
# # Input Validation: 
# def check_is_number(value):
#   return isinstance(value, (int, float))