import random

counter = 0
heads = 0
tails = 0
result = 0

while counter != 100:
    counter += 1
    result = random.randint(1, 2)
    if result == 1:
        heads += 1
    elif result == 2:
        tails += 1

print("I flipped the coin", counter, "times.\n"\
      "Tails came up", tails, "number of times.\n"\
      "Heads came up", heads, "number of times.")
