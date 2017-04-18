#Hangman game new try
#you can get indices from strings '-.-

import random

wordtuple = ("Eisenbahn", "Persocom", "Nerd", "Weltherrschaft", "Softwareentwicklung",\
         "Weltschmerz", "Zeitgeist", "Pickelhaube")

WORD = random.choice(wordtuple).upper()
word_guess = "_" * len(WORD)
word_wrong = ""
guess_counter = 0

print(WORD)

while word_guess != WORD and guess_counter < 5:
    guess = input("\nGuess another letter: ").upper()
    if guess not in WORD:
        if guess in word_wrong:
            print("\nNo matter how often you try, it's not in the word!")
            continue
        else:
            guess_counter += 1
            word_wrong += guess

    else:
        if guess in word_guess:
            print("\nYou already know that", guess, "is part of the word.")
            continue
        else:
            word_empty = ""
            for i in range(len(WORD)):
                if WORD[i] == guess:
                    word_empty += guess
                else:
                    word_empty += word_guess[i]
            word_guess = word_empty

    print("\tThe Good: ", word_guess)
    print("\tThe Bad: ", word_wrong)
    print("\tThe Number: ", guess_counter)
