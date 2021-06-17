print("Hi! This code will require you to input two numbers.")
print("This code will also tell you if the numbers inputted are either")
print('"ODD" or "EVEN". Thereafter, it will also tell you if one number is')
print("greater than the other or if they are equal to each other.")


Num1 = input("\nGive me a number: ")
# This line of code represents the input for the first number
# by putting "try" here, this 
# will help us handle expected and unexpected.
# errors in our code.
try:
    modNum1 = int(Num1)
    if modNum1%2 == 0:
        print("\tThe entered number is EVEN.\n")
    else:
        print("\tThe entered number is ODD.\n")
# Try and Except should be on the same indention level in order 
# to work. Same goes with if, elif, and else.
except:
    print("Input is invalid.\n")

# This line of code represents the input of the second number
Num2 = input("Give me another number: ")

try:
    modNum2 = int(Num2)
    if modNum2%2 == 0:
        print("\tThe entered number is EVEN.\n")
    else:
        print("\tThe entered number is ODD.\n")

except:
    print("Input is invalid.\n")

try:
    if modNum1 > modNum2:
        print(modNum1, "is greater than", str(modNum2) + ".")
    elif modNum2 > modNum1:
        print(modNum2, "is greater than", str(modNum1) + ".")
    else:
        print("Both numbers are equal.\n")
# Str was used in order to concatenate the integer and the "." 
# for formatting purposes

# elif will only be used if there is more than 2 conditions.

except:
    print("One or more of the entered numbers is invalid.")

