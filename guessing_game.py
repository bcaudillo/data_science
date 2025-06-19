import random


number = random.randint(1,10)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    user_guess = int(input("Please enter a number between 1 and 10: "))
    attempts += 1
    attempts_left = 5 - attempts
    if user_guess == number:
        print("You win!")
        attempts = 6
    elif user_guess <= 0:
        print("You must enter a number 1-10.")
    elif attempts <= 0:
        print("You lose!")
    else: 
        print(f"You have {attempts_left} attempts left. Guess again.")
        





