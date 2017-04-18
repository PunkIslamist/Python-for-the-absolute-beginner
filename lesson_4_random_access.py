import random

word = input("Please enter a word:\n")

length_low = -len(word)
length_high = len(word)

for i in range(10):
    pos = random.randrange(length_low, length_high)
    print("The letter at position", pos, "is", word[pos])
