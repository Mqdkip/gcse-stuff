import random
hidden_number = random.randint(1,6)
user_guess = int(input("Input a number from 1 to 6: "))
guess = 1

if not isinstance (user_guess,int):
    raise ValueError("Input must be an integer")

if user_guess > 6:
    raise ValueError("Input cannot be greater than 6")
elif user_guess < 1:
    raise ValueError("Input cannot be less than 1")

else:
    while user_guess != hidden_number:
        print("unlucky")
        user_guess = int(input("Input a number from 1 to 6: "))
        guess += 1
        

    print(f"Good job guessing, it took you {guess} guesses")
      



