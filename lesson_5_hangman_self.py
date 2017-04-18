#Hangman game
#[x] wordlist
#[x] pick a word
#[x] for each letter print an underscore
#[x] get player guesses
#[x] change underscores for correct guesses
#[ ] advance hangman for wrong guesses
#[ ] good finish when word completed
#[ ] bad finish when hangman completed

import random

wordtuple = ("Eisenbahn", "Persocom", "Nerd", "Weltherrschaft", "Softwareentwicklung",\
         "Weltschmerz", "Zeitgeist", "Pickelhaube")

WORD = wordtuple[random.randrange(len(wordtuple))].upper()
print(WORD)

#PREPERATION STAGE
#create list from picked word with letters as invidividual entries
word_l = []
for letter in WORD:
    word_l.append(letter)
    print(word_l)

#create list word_guess with underscores
word_guess = []
for letter in WORD:
    word_guess.append("_")
    print(word_guess)




guess_amount = 0
guess_wrong = []
while guess_amount < 4:
    if "_" not in word_guess:
        break
    guess = input("\n\nYour next guess: ").upper()
    if guess in WORD:
        if guess in word_guess:
            print("You already guessed that one!")
            continue

        #write letter in word_guess
        #replace letter with 0s in word_l
        else:        
            while guess in word_l:
                pos = word_l.index(guess)
                word_guess[pos] = guess
                word_l[pos] = 0
            print("Yay,", guess, "is part of the word!\n")
        
    elif guess not in WORD:
        if guess in guess_wrong:
            print("Nope, still not part of the word '-.-")
            continue
        else:
            print("Sorry,", guess, "is not part of the word.\n")
            guess_wrong.append(guess)
            guess_amount += 1

           
    print("Correct:", end=" ")
    for i in word_guess:        
        print(i, end=" ")
    print()
    print("Incorrect:", end= " ")
    for i in guess_wrong:
        print(i, end=" ")
    print()
    print("Wrong guesses:", guess_amount)

if guess_amount == 4:
    print("""
\t\toooooooo
\t\t HUARGH
\t\toooooooo
    """)
elif "_" not in word_guess:
    print("""
\t\t!!!!!!!!!!!!!
\t\tWe haz winner
\t\t!!!!!!!!!!!!!
    """)
