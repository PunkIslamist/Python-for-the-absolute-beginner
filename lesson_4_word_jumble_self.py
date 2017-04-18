# trying to create the world jumble game
# [x] create bunch of words to chose from
# [x] pick a word
# [x]jumble word
# [x]show jumbled word
# [x]take guesses
# [x]if correct, yay
# [x]if wrong, take new guess

import random

wordlist = ("Eisenbahn", "Persocom", "Nerd", "Weltherrschaft", "Softwareentwicklung",\
         "Weltschmerz", "Zeitgeist", "Pickelhaube")

word = wordlist[random.randrange(0, len(wordlist))]
#Alternative: word = random.choice(wordlist)

WORD = word
word_j = ""
pos = None

while word:
    pos = random.randrange(len(word))
    word_j += word[pos]
    word = word[:pos] + word[pos+1:]

print("Hokay, the jumbled word is:\n", word_j)

guess = input("\nWhich word would you think this mess is?\n")
while guess.lower() != WORD.lower():
    print("\nSorry mate, no correct!")
    guess = input("\nYour new guess:\n")

print("Nooooice, your guess '",guess.capitalize(),"' was indeed my original word", WORD,".")
