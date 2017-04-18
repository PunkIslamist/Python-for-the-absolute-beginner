#Get input and play around with it

name = input("Hello, please tell me your name:\n")

print()
print(name.capitalize(), ", nice to meet you! How old are you?")
age = int(input())

print()
weight = float(input("Now I only need your weight and we are done:\n"))

print()
print()
fun = "let the fun begin!"
print(fun.upper())

print()
print(name.upper())
print(name.lower())
print(name*10)


print()
age_seconds = age*365*24*360
print("Did you know that you are", age_seconds, "seconds old?")

print()
weight_moon = weight/6
weight_sun = weight*27.1
print("You probably also did not know that your weight on the moon would be",\
      weight_moon, "kilograms. On the sun however it would be",\
      weight_sun, "kilograms. AMAZING!")
