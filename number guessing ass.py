import random

print('guess the Number (1 to 100)')

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

guess = None

# Loop until user guesses the correct number
while guess != secret_number:
    # Ask for input and convert to int
    guess = int(input('Enter your guess: '))

    # Check guess against the secret number
    if guess < secret_number:
        print('Too low! oops.')
    elif guess > secret_number:
        print('Too high! oops.')
    else:
        print('hurray Correct! You guessed the number.')

