# Library log in prototype
# Bartosz Iwaszkiewicz, Jack Williams
# 19.04.2022


#Log in function

def library_login():
    if input("Please input library password (it's 'bee_gees'): ") == library_password:
        main()
    else:       
        print("wrong password")

# Main Library password

library_password = "bee_gees"

# Main Library database

lst = ['item1', 'item2', 'item3']

# Show Main Library Database function

def main_database():
    print(lst)

# Main add, show, remove loop

def main():
    while True:
        option = input("What would you like to do? Select from options: add (add a new library item), show (show all library items), remove (remove a library item from the list) ")
        if option == "add":
            item = input("Please input a new Library Item ")
            lst.append(item)
            print("The item has been successfully added to the Library Database ")
        elif option == "show":
            print("\n")
            main_database()
            print("--------------------------------\n")
        elif option == "remove":
            item_to_be_removed = input("Please type the item you want removed ")
            for i, list_item in enumerate(lst):
                if list_item == item_to_be_removed:
                    lst.pop(i)
                    print("The item has been successfully removed from the Library Database ")
                    break
            else:
                print('Item not found ')
        else:
            print('Invalid option ')

# Start the program

while True:
    library_login()
