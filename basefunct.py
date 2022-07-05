loop = True #set to false when program is ending
print("Welcome to the class diagnostic program.\n\n")
#TODO: set up the lists filled with the data we're keeping stored, or maybe a list of dicts
while loop == True:
    print("MAIN MENU:\n")
    print("a. Display Classes\nb. Enter a New Class\nc. Exit Program")
    choice = input("Please enter an option: ")
    if choice == "a":
        pass #display the classes that have been entered
    elif choice == "b":
        pass #enter a new class
    elif choice == "c":
        loop = False
        break
    else:
        print("This was not a valid input.")
        continue