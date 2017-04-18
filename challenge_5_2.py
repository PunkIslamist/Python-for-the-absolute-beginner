# Charactor Creator
# user can spend 30 attribute points in total
# on 4 attributes
# can always add or remove points from attributes

CHOICES = ("0", "1", "2", "3", "4")
att_points = 30
att = [["dex", 0], ["dik", 0], ["int", 0], ["tit", 0]]


#MAIN MENU
choice_menu = ""
while choice_menu != "0":
    print("""
\t~MAIN MENU~
[1] Add points to an attribute
[2] Remove points from an attribute
[3] Show Attributes
[0] Exit
    """)    
    choice_menu = input("What do you want to do? ")
    while choice_menu not in CHOICES:
        choice_menu = input("\nSorry, that is not an option. Please make a valid choice: ")

    
#ADDING POINTS
    if choice_menu == "1":        
        print("""

[1] Dexterity
[2] Penissize
[3] Intelligence
[4] Breastsize
[0] Back to Main Menu""")
        choice_att_add = input("\nWhich attribute do you want to raise? ")
        while choice_att_add not in CHOICES:
            print("\nSorry, this is not a valid choice.")
            print("Try again:", end=" ")
            choice_att_add = input()

        if choice_att_add == "0":
            continue

        else:
            att_add = att[int(choice_att_add) -1]
            print("How many points of your", att_points, "points do you want to add?", end=" ")
            add_amount = int(input())
            while add_amount > att_points:
                print("\nSorry, you can spend only up to", att_points, "points.")
                add_amount = int(input("How many points do you want to spend? "))
            att_add[1] += add_amount
            att_points -= add_amount
    

#REMOVING POINTS
    if choice_menu == "2":
        print("""

[1] Dexterity
[2] Penissize
[3] Intelligence
[4] Breastsize
[0] Back to Main Menu""")
        choice_att_low = input("\nWhich attribute do you want to lower? ")
        while choice_att_low not in CHOICES:
            print("\nSorry, this is not a valid choice.")
            print("Try again:", end=" ")
            choice_att_low = input()

        if choice_att_low == "0":
            continue

        else:
            att_low = att[int(choice_att_low) -1]
            print("How much do you want to lower it? Its currently at", att_low[1], end=": ")
            low_amount = int(input())
            while low_amount > att_low[1]:
                print("\nSorry, you can remove only up to", att_low[1], "points.")
                low_amount = int(input("How many points do you want to remove? "))
            att_low[1] -= low_amount
            att_points += low_amount

#ATTRIBUTE SCREEN
    if choice_menu == "3":
        print("\n\n")
        print("---------------------------")
        print("ATTRIBUTE POINTS:\t", att_points)
        print("DEXTERITY:       \t", att[0][1])
        print("PENISSIZE:       \t", att[1][1])
        print("INTELLIGENCE:    \t", att[2][1])
        print("BREASTSIZE:      \t", att[3][1])
        print("---------------------------")

print("\n\nrip in pepperoni")
print("   ~(x__x)~")
input()
