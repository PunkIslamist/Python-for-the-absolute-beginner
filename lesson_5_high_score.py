#add or remove items from a list
#uses list methods

scores = []
choice = None

while choice != 5:
    print("""
 1 - Show Scores
 2 - Add a Score
 3 - Remove a Score
 4 - Sort Scores
 5 - Exit
 """)

    choice = int(input("Choice: "))
    print()

    if choice == 5:
        print("Sayonara!")

    elif choice == 1:
        print("Scores:\n")
        for i in scores:
            print(i)

    elif choice == 2:
        score = int(input("Enter a score: "))
        scores.append(score)

    elif choice == 3:
        score = int(input("Which score do you want to remove? "))
        if score in scores:
            scores.remove(score)

    elif choice == 4:
        scores.sort(reverse=True)

    else:
        print("Sorry,", choice, "is not a valid choice.")

