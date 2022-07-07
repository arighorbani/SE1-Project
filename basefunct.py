def newClass():
    coursename = input("Please enter the name of the course: ")
    term_str = input("Please enter the term in which you took the course: ")
    term = term_str.split(" ")
    grade = float(input("Please enter the percentage-based grade you got in this course: "))
    profname = input("Please enter the name of your professor for this course: ")
    courserating = int(input("Please enter how you would rate the course from 1 to 10: ")) #TODO:errorcheck
    profrating = int(input("Please enter how you would rate the professor from 1 to 10: ")) #TODO: errorcheck
    currclass = [coursename, term, grade, profname, courserating, profrating]
    return currclass

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
            #TODO: loop on the display of classes
            whichclass = 1
            for x in classlist:
                print(str(whichclass) + ".       Course name: "  + x[0] + '\n')
                whichclass += 1
                print("         Term: " + x[1][0] + " " + x[1][1] + '\n') #TODO: make this info sortable!
                print("         Grade: " + str(x[2]) + '\n')
                print("         Professor's Name: " + x[3] + '\n')
                print("         Course Rating: " + str(x[4]))
                print("         Professor's Rating: " + str(x[5]) + "\n\n\n")
            #TODO: translate the percentage-based grade  the user entered into a letter grade
            
            print("a. Sort Classes by Term (NOT CURRENTLY WORKING)") #TODO: implement sort
            print("b. Enter New Class")
            print("c. Exit Program")
            choice = input("Please enter an option: ")
            if choice == "a":
                pass
            elif choice == "b":
                classlist.append(newClass())
            elif choice == "c":
                break


        else: #THERE ARE NO CLASSES STORED
            print("There are no classes stored.\nReturning to main menu\n")
            continue
    elif choice == "b": #entering a new class
        classlist.append(newClass())


    elif choice == "c": #exit program
        break
    else:
        print("This was not a valid input.")
        continue

print("\nYou are now exiting the program; thank you for using it!")