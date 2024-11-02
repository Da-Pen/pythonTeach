
# Exercise: create an interactive "Python dictionary": a dictionary where the key is a Python concept or keyword, and
# the value is a description of what it's used for. The user is presented with this menu:
# Choose what to do:
# (1) Look up definition
#     - Which Python concept would you like to get the definition of?
# (2) Add / modify definition
#     - Which Python concept would you like to add / modify?
#     - What would you like the definition of "x" to be?
# (3) Remove dictionary item
#     - Which Python concept would you like to remove?
# (4) Clear dictionary
# (5) Get number of items in dictionary
# (6) Print all dictionary terms
# (7) Exit program

def python_dictionary():
    python_dict = {}
    while True:
        choice = input("""-----
Choose what to do:
    (1) Look up definition
    (2) Add / modify definition
    (3) Remove dictionary item
    (4) Clear dictionary
    (5) Get number of items in dictionary
    (6) Print all dictionary terms
    (7) Exit program
""")
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Not a valid choice")
            continue

        choice = int(choice)
        if choice == 1:  # Get definition
            concept = input("Which Python concept would you like to get the definition of?\n")
            if concept in python_dict:
                print(f'The definition of "{concept}" is: {python_dict[concept]}')
            else:
                print(f'No definition for "{concept}"')

        elif choice == 2:  # Add / modify definition
            concept = input("Which Python concept would you like to add / modify?\n")
            definition = input(f'What would you like the definition of "{concept}" to be?\n')
            python_dict[concept] = definition
            print(f'Your Python dictionary now has the definition "{concept}": {definition}')

        elif choice == 3:  # Remove definition
            concept = input("Which Python concept would you like to remove?\n")
            if concept in python_dict:
                python_dict.pop(concept)
                print(f'"{concept}" removed')
            else:
                print(f'"{concept}" doesn\'t exist in the dictionary!')

        elif choice == 4:  # Clear dictionary
            python_dict.clear()
            print("Dictionary cleared")

        elif choice == 5:  # Number of items in dictionary
            print(f"There are {len(python_dict)} item(s) in the dictionary")

        elif choice == 6:  # Print all dictionary items
            for concept in python_dict:
                print(f"\t{concept}: {python_dict[concept]}")

        else:
            print("Exiting program...")
            exit()


python_dictionary()

# Challenge exercise: create an application where the user can keep track of countries and their official languages.
# Can add / remove languages for any country.