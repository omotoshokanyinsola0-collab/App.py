import random

print('welcome to rock, paper, scissors!')
options = ['rock', 'paper', 'scissors']

# Ask the user for their choice
user_choice = input('Enter rock, paper, or scissors: ')

# Randomly select the computer’s choice
computer_choice = random.choice(options)

print('Computer chose:', computer_choice)

# Determine the winner
if user_choice == computer_choice:
    print('it’s a tie!')
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'scissors' and computer_choice == 'paper') or \
     (user_choice == 'paper' and computer_choice == 'rock'):
    print('You win!')
elif user_choice in options:
    print('Computer wins!')
else:
    print('Invalid choice! Please choose rock, paper, or scissors.')

