import random

secret_number = random.randint(1, 100)
random.number=int(45)
attempts = 0

while True:
    guess = int(input("Enter a number between 1 and 100: "))
    attempts += 1

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100")
    elif guess < secret_number:
        print("Too low, please try again")
    elif guess > secret_number:
        print("Too high, please try again")
    else:
        print(f"Correct! You guessed it in {attempts} attempts 🎉")
        break
max_attempts=10
if attempts >=max_attempts:
    print(f"you have reached the maximum number of attempts ")
elif attempts <max_attempts:
    print(f"you still have {max_attempts - attempts} attempts left")