#Author: Colton Graham
#Date: 10/29/2021
#Filename: groupAssignment
#Description: A program for a group assignment

#Custom method
def thing(double1, double2, string):

    print()
    print("The first number you chose was: " + str(double1))
    print("The second number you chose was: " + str(double2))
    print()

    total = double1 + double2
    print("Your two numbers added together are: " + str(total))
    print()

    if total <= 0:
        print("The text you entered was: " + string)
        print()
    
    else: 
        print("The text your entered was not: " + string)
        print()

    print("Number 1 divided by number 2 is: " + str(double1/double2))
    print()

    print(string.upper())
    print()


#Take user input
while True:
    double1 = (input("Enter a number: "))
    
    #Error Trapping
    if double1.isnumeric():
        double1 = int(double1)
        break
    else:
        print("Error! Enter a number")
        continue

#Take user input
while True:
    double2 = (input("Enter another number: "))

    #Error trapping
    if double2.isnumeric():
        double2 = int(double2)
        break
    else:
        print("Error! Enter a number")
        continue

#Take user input
while True:
    string1 = input("Enter any text (must be at least 10 characters): ")
    length = len(string1)

    #Make sure the string is 10 characters
    if length >= 10:
        break
    else:
        print("Not enough characters")
        continue

#Call thing
try:
    thing(double1, double2, string1)
    
    #####Try#####
    # - thing(14.6, 17.2, "fdgjkdfghjk")
    # - thing(2, 4, "dddddddddddd")
    # - thing(1, 1, "111111111111")

except:     #Error trap
    print("Parameters were entered incorrectly, they should be: double, double, string")
