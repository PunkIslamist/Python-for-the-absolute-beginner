print("Counting:")
for i in range(10):
    print(i+1, end=" ")

print("\n\nCounting by  fives:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("Backwards we go!")
for i in range(10, 0, -1):
    print(i, end=" ")


j = 0
for i in "Eisenbahnschiene":
    j += 1
print("\n\nDas Wort 'Eisenbahnschiene' besteht aus:", j, "Buchstaben")
