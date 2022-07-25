#FOR MICROSERVICE: https://www.youtube.com/watch?v=JTSxXwDO-Lg

from operator import itemgetter


def newClass(): #function that takes new class input and makes a new object out of it
    coursename = input("Please enter the name of the course: ")
    term_str = input("Please enter the term in which you took the course: ")
    term = term_str.split(" ")
    term[1] = int(term[1])
    grade = float(input("Please enter the percentage-based grade you got in this course: "))
    profname = input("Please enter the name of your professor for this course: ")
    courserating = int(input("Please enter how you would rate the course from 1 to 10: ")) #TODO:errorcheck
    profrating = int(input("Please enter how you would rate the professor from 1 to 10: ")) #TODO: errorcheck
    currclass = [coursename, term, grade, profname, courserating, profrating]
    return currclass

def printClasses(listoflists): #print classes from classlist
    whichclass = 1
    for x in listoflists:
        print("\n" + str(whichclass) + ".       Course name: "  + x[0])
        whichclass += 1
        print("         Term: " + x[1][0] + " " + str(x[1][1])) #TODO: make this info sortable by season as well!
        print("         Grade: " + str(x[2]) + "%")
        print("         Professor's Name: " + x[3])
        print("         Course Rating: " + str(x[4]))
        print("         Professor's Rating: " + str(x[5]) + "\n")

def sortClasses(listoflists): #sort classes as user chooses to
    listoflists.sort(key=lambda x:x[1][1])
    while True:
        sortchoice = input("a. Sort earliest to latest\nb. Sort latest to earliest\nPlease enter an option: ")
        if(sortchoice == "a"):
            break
        elif(sortchoice == "b"):
            listoflists.reverse()
            break
        else:
            print("This is not a valid option. Please try again.\n")



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
            printClasses(classlist)
            #TODO: translate the percentage-based grade  the user entered into a letter grade
            
            print("a. Sort Classes by Term")
            print("b. Enter New Class")
            print("c. Exit Program")
            choice = input("Please enter an option: ")
            if choice == "a":
                sortClasses(classlist)
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