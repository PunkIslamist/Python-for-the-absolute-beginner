#create empty tuple
#ask for 3 inputs
#add each input to tuple then print tuple

tuple = ()

item_1 = input("\nPlease give me your first item!\n")
item_2 = input("\nNow, what's your second item?\n")
item_3 = input("\nAnd the final one?\n")

tuple = (item_1, item_2, item_3)
print(tuple)

for item in tuple:
    print(item)
