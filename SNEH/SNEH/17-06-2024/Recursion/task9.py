import random

lower_bound = 1
upper_bound = 1000
max_attempts = 10

secret_number = random.randint(lower_bound, upper_bound)


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "To low"
    else:
        return "To high"
    



for i in range (1,5):
    guess=int(input("Enter a Number:"))

    x=check_guess(guess, secret_number)
    print(x)
    
    if x == "Correct":
        print("You've guessed the correct number")
        break
else:
    print("Sorry, you've used all your attempts.")