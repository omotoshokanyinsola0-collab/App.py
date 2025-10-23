from datetime import datetime

print('age in days Calculator')

# Ask the user to enter birthdate in YYYY-MM-DD format
birthdate_str = input('Enter your birthdate (YYYY-MM-DD): ')

# Convert string to datetime object
birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')

# Get today’s date
today = datetime.today()

# Calculate age in days
age_in_days = (today-birthdate).days

print(f'You are {age_in_days} days old.')










