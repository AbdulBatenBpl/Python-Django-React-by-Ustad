import random

secret_number = random.randint(1,100)

attempt = 0

while True:
    try:
        guess = int(input("Guess a number between 1 to 100: "))

        if guess == secret_number:
            attempt += 1
            print("Congratulations! You've guessed the number in {} attempts".format(attempt))
            break
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")
        attempt += 1
    except ValueError:
        print("Invalid input! Please enter a number")
