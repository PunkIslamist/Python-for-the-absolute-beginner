import random

#random integer between and including 1-6
die_1 = random.randint(1, 6)

#randrange starts counting from 0, so the following does the same as the first line
die_2 = random.randrange(6) +1

total = die_1 + die_2

print(die_1)
print(die_2)
print(total)
