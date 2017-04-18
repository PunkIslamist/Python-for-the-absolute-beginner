#have user add or remove items from tuple
#[x] create empty tuple
#[x] ask user if he wants to add or remove an item
#[x] if 'add' concatenate tuples
#[x] if 'remove' create new tuple

inventory = ()
inventory_new = ()
item_add = ()
item_remove = ""


while True:
    choice = input("Do you want to 'add' or 'remove' an item from your inventory?\n")
    if choice.lower() == "add":
        item_add = (input("Which item do you want to add?\n"),)
        inventory += item_add
        print("Your inventory now:", inventory)

    elif choice.lower() == "remove":
        item_remove = input("Which item do you want to remove?\n")
        for item in inventory:
            if item.lower() != item_remove.lower():
                inventory_new += (item,)

            elif item == item_remove.lower():
                continue

        inventory = inventory_new
        inventory_new = ()
        print(inventory)
