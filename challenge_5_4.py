#WHO'S YOUR (GRAND)DADDY?
#dictionary with son-dad relationships
#user can add, change, remove entries
#can ask "who is dad of 'x'?"

#DICTIONARY/FAMILY TREE/DADDY DATABASE (DD)

DD = {"a_a_a":"a_a", "a_a_b":"a_a", "a_a_b":"a_a", "a_b_a":"a_b", "a_b_b":"a_b", "a_b_c":"a_b",\
      "a_a":"a", "a_b":"a",\
      "b_a_a":"b_a", "b_a_b":"b_a", "b_a_c":"b_a", "b_b_a":"b_b", "b_b_b":"b_b", "b_b_c":"b_b",\
      "b_a":"b", "b_b":"b"}

choice_menu_m = ""

while choice_menu_m != "0":
    #MAIN MENU
    print("""
[1] Check a dad
[2] Check a granddad
[3] Edit the family tree
[4] Check entries in the tree
[0] Exit
""")
    choice_menu_m = input("Waddaya wanna do?\n")

    if choice_menu_m == "1":
        #SHOW FATHER OF USER INPUT
        father_request = input("\nWhose father you want to look up?\n")
        fnope = "\nSorry, I don't have information on the father of "
        dad = DD.get(father_request, fnope + father_request)
        print("\nThe daddy of", father_request, "would be", dad, end=".\n")
        input()

    elif choice_menu_m == "2":
        #SHOW GRANDDADDY OF USER INPUT
        gfather_request = input("\nWhose granddad you wanna look up?\n")
        gnope = "\nSorry, I don't have information on the granddad of "
        gdad = DD.get(DD.get(gfather_request), gnope + gfather_request)
        print("\nThe granddad of", gfather_request, "would be", gdad, end=".\n")
        input()

    elif choice_menu_m == "4":
        #PRINT ALL KEYS
        for i in DD.keys():
            print(i)
            
    elif choice_menu_m == "3":
        #EDIT MENU        
        choice_menu_e = ""
        while choice_menu_e != "0":
            print("""
[1] Add an entry
[2] Edit an entry
[3] Remove an entry
[0] Back to Main Menu
""")
            choice_menu_e = input("\nWhat do you want to edit?\n")
            if choice_menu_e == "1":
                #ADD AN ENTRY
                print("First tell me the son's name: ")
                son_new = input()
                if son_new not in DD:                    
                    print("And now his father's name: ")
                    dad_new = input()
                    DD[son_new] = dad_new
                    print()
                    print(dad_new, "is now the father of", son_new, end=".")
                    input()
                else:
                    print(son_new, "is already an entry. Please use 'Edit' if you want to edit his entry.")
                    input()

            elif choice_menu_e == "3":
                #REMOVE AN ENTRY
                print("\nWhom do you want to remove?\n")
                for i in DD.keys():
                    print(i)
                delete = input("\nRemove: ")
                if delete in DD:
                    del DD[delete]
                    print("Ok,", delete, "is no more. RIP!")
                    input()
                else:
                    print("Sorry,", delete, "is not in the family tree.")

            elif choice_menu_e == "2":
                #EDIT AN ENTRY
                print("\nChoose an entry to edit:")
                for i in DD:
                    print(i)
                print()
                edit = input()
                if edit in DD:
                    print("\nPlease enter the new name for", edit, "or press Enter to continue.")
                    son_new = input()
                    print("Now enter the name for", DD[edit], "or press Enter to keep", DD[edit], end=":\n")
                    dad_new = input()
                    if son_new == "" or son_new == edit:
                        if dad_new == "" or dad_new == DD[edit]:
                            print("\nWell ok then, you changed nothing. Good job!")
                            continue
                        else:
                            DD[edit] = dad_new
                        
