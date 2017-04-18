# word guessing game
# PC picks random word from list
# PC tells user how many letters there are in the word
# user can ask 5 times if a letter is in the word
# PC answers yes or no
# after 5 tries user has to enter a guess
# PC tells user if guess was right or wrong

import random

wordlist = ("Eisenbahn", "Persocom", "Nerd", "Weltherrschaft", "Softwareentwicklung",\
         "Weltschmerz", "Zeitgeist", "Pickelhaube")

# pick word and tell length of word
word = wordlist[random.randrange(len(wordlist))]
print(word)
print("The word I am thinking of consists of", len(word), "letters.")

#get questions about letters
que = ""
que_amount = 0
let_correct = ""
let_wrong = ""

while que_amount < 5:
    que_amount += 1
    que = input("\nAsk me a letter:\n")

    if que.lower() in word.lower():
        print("Yes,", que.upper(), "is in the word I am thinking of.")
        let_correct += que.upper()
    elif que.lower() not in word.lower():
        print("Sorry,", que.upper(), "is not part of my word.")
        let_wrong += que.upper()


#present information about asked letters
#ask for word guess
#evaluate guess
print("\n\nLetters in my word are:\n",let_correct)
print("Not included are:\n",let_wrong)
guess = input("\n\nWhat do you think is the word I am thinking off?\n")
if guess.lower() == word.lower():
    print("Indeed, I was thinking of", word,". Well done!")
elif guess.lower() != word.lower():
    print("Sorry, I was not thinking of", guess.capitalize(),". My word was", word,".")
