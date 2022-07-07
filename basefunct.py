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
            whichclass = 1
            for x in classlist:
                print(whichclass + ".        Course name: "  + x[0] + '\n')
                whichclass += 1
                print("         Term: " + x[1][0] + " " + x[1][1] + '\n') #TODO: make this info sortable!
                print("         Grade: " + x[2] + '\n')
                print("         Professor's Name: " + x[3] + '\n')
                print("         Course Rating: " + x[4])
                print("         Professor's Rating: " + x[5] + "\n\n\n")
            #TODO: translate the percentage-based grade  the user entered into a letter grade
            print("a. Sort Classes by Term (NOT CURRENTLY WORKING)") #TODO: implement sort
            print("b. Enter New Class")
            print("c. Exit Program")
            choice = input("Please enter an option: ")
            #TODO: MAKE ENTERING A NEW CLASS AND SORTING INTO SEPARATE FUNCTIONS!!!
            #TODO: place the usage of choice here (VITAL)
        else: #THERE ARE NO CLASSES STORED
            print("There are no classes stored.\nReturning to main menu\n")
            continue
    elif choice == "b": #entering a new class TURN INTO FUNCTION
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