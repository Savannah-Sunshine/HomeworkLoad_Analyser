# Input:
# read a file that contains all the homework input
#       file also has start_date and end_date
# make it canvas & learning suite readable? ... inport from both?
# organise that homework with its classes, weight, name
#    (if it has the word project, essays, test, then it is heavier)
def readInput():
  import sys

  #if not enough arguments
  if len(sys.argv) < 2:
    print("failed")
    raise Exception("No file attached")

  with open(sys.argv[1], 'r') as file:
    for line in file:
        print(line)

    file.close()
    print("did it")






# Output:
# based on command of user
#   B:  Get the busiest week (most # of homework)
#   B_Many:  Get the busiest weeks
#   L:       Get the lightest week (least # of homework)
#   L_Many:  Get the lightest/easiest weeks
#   All:     Prints out every week with # of hw & output is colored?
#               realitively to its "easiness"
def whichOutput(input):
    input = input.lower()
    if input == "b":
        #Get the busiest week (most # of homework)
        print("TODO")
    elif input == "b_many":
        #Get the busiest weeks
        print("TODO")
    elif input == "l":
        #Get the lightest week (least # of homework)
        print("TODO")
    elif input == "l_many":
        #Get the lightest/easiest weeks
        print("TODO")
    elif input == "all":
        #Prints out every week with # of hw & output is colored?
        print("TODO")
    elif (input == "quit" or input == "q"):
        #Ends program
        print("Goodbye\n")
        return 0;
    elif input == "commands":
        #Prints out list of commands
        print("B        Busiest week")
        print("B_Many   Busiest weeks")
        print("L        Easiest week")
        print("L_Many   Easiest weeks")
        print("All      Every week")
        print("Quit     Quits program\n")
    else:
        print("Invalid input, please try again\n")
    return 1




#main
#begins the program

#reads file
readInput()

#takes input from user
continueProg = whichOutput( input("Enter command: ") )
while continueProg:
    continueProg = whichOutput( input("Enter command: ") )
