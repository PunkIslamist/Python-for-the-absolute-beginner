#Number guessing game self-made

#create random number
import random
number = random.randrange(100) +1



#get input and loop
guess_input = 0
guess_amount = 0
tries = 0

while guess_input != number and tries < 5:
    guess_amount += 1
    tries += 1
    guess_input = int(input("Your guess:\n"))

    if guess_input < number:
        print("Sorry, too low. Try again!")

    elif guess_input > number:
        print("Nope, too high this time. Try once more!")

if guess_input == number:
    print("HELL YEAH!", number, "was the right guess!\n"\
          "Fucking nito man!\n"\
          "It took you", guess_amount, "tries.")

else:
    print("Sorry, you already used your", tries, "tries :(")
