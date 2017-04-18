#PC picks from a wordlist
#random order
#picked word gets printed
#PC has to pick every word, no word more than once
import random

wordlist = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n")

selector = []
for i in range(len(wordlist)):
    selector.append(i)
    print(selector)

while selector:
    index = random.choice(selector)
    print(wordlist[index])
    selector.remove(index)
