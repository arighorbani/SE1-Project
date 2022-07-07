loop = True #set to false when program is ending
print("Welcome to the class diagnostic program.\n\n")
classlist = [] #list of lists, containing coursename, term, grade, profname, courserating, and profrating
while loop == True:
    print("MAIN MENU:\n")
    print("a. Display Classes\nb. Enter a New Class\nc. Exit Program")
    choice = input("Please enter an option: ")
    if choice == "a":
        #display the classes that have been entered
        if bool(classlist):
            pass #display
            #TODO: decide how to display the data stored inside of classlist
            #TODO: decide what the available options should be once list is displayed
            #TODO: find out how to properly sort based on which season a term was taken as well
            #TODO: translate the percentage-based grade  the user entered into a letter grade
        else: #THERE ARE NO CLASSES STORED
            print("There are no classes stored.\nReturning to main menu\n")
            continue
    elif choice == "b": #entering a new class
        #TODO: error checking on each of the inputs that need error checking
        coursename = input("Please enter the name of the course: ")
        term_str = input("Please enter the term in which you took the course: ")
        term = term_str.split(" ")
        grade = float(input("Please enter the percentage-based grade you got in this course: "))
        profname = input("Please enter the name of your professor for this course: ")
        courserating = int(input("Please enter how you would rate the course from 1 to 10: ")) #TODO:errorcheck
        profrating = int(input("Please enter how you would rate the professor from 1 to 10: ")) #TODO: errorcheck
        currclass = [coursename, term, grade, profname, courserating, profrating]
        classlist.append(currclass)
        

    elif choice == "c": #exit program
        break
    else:
        print("This was not a valid input.")
        continue

print("\nYou are now exiting the program; thank you for using it!")