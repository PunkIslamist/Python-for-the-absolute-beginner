# Player enters a number and the PC tries to guess the number
# Show each try, then automatically evaluate if correct, too high or too low
# if not correct, take new guess based on too high or too low
# if correct, show correct number and number of guesses

import random

number = int(input("Please enter a number between 1 and 100:\n"))
while number < 1 or number > 100:
    number = int(input("This number is not between 1 and 100.\nPlease enter a a number between 1 and 100:\n"))

guess_amount = 1
guess_number = random.randint(1, 100)
guess_lowest = 0
guess_highest = 101

while guess_number != number:
    guess_amount += 1
    print("\nMy guess is", guess_number)

    if guess_number > number:
        print("\nDamn, that was too high!")
        guess_highest = guess_number
        
    elif guess_number < number:
        print("\nShitfuck, that's too low!")
        guess_lowest = guess_number

    guess_number = random.randint(guess_lowest +1, guess_highest -1)
print("\nMy guess is", guess_number)
print("\nYay,", guess_number, "was correct!\n"\
      "It took me a total of", guess_amount, "tries to figure that one out.")
