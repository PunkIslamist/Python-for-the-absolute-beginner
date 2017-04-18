#Score Program 2.0 - NOW WITH NAMES

scores = []
choice = None

while choice != 3:
    print("""
 1 - List Scores
 2 - Add a Score
 3 - Exit
 """)

    choice = int(input("Your choice: "))
    print()

    if choice == 3:
        print("Sayonara!")

    elif choice == 1:
        print("Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    elif choice == 2:
        name = input("Player's name?: ")
        score = int(input("His or her score?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)

    else:
        print("Sorry, that is not a valid choice,")
    
