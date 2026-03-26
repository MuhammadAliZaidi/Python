# Import only the 'choice' function from random module
from random import choice

# Randomly select either 'head' or 'tail' from the list
coin = choice(['head', 'tail'])
print(coin)


# Import the full random module
import random

# Create a list of cards
cards = ['jack', 'king', 'queen']

# Shuffle (randomly rearrange) the list
random.shuffle(cards)

# Loop through each card and print it
for card in cards:
    print(card)


# Generate a random integer between 1 and 10 (inclusive)
print(random.randint(1, 10))


# Print blank lines for spacing
print()
print()


# Import mean function from statistics module
from statistics import mean

# Calculate and print the average of the list
print(mean([100, 80]))   # Output will be 90


# Print another blank line
print()


# Import sys module to access command-line arguments
import sys

# Print the first command-line argument (not user input!)
# sys.argv[0] = file name
# sys.argv[1] = first argument passed when running the program
print('My name is ', sys.argv[1])
