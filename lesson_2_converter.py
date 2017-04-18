print("Hello and welcome to the Conversion Example Program!")

print()
print()

name = (input("Please tell me your name:\n"))

print()

#input() ist mit mehr als einem Argument überfordert - print() it aint!
print("Ok,", name.capitalize(),", now I need your height:")
height = float(input())

print()

age = int(input("And finally your age:\n"))

print()

print("So,", name.capitalize(), ", you are", height, \
      "metres tall and", age, "years old. Noice!")
