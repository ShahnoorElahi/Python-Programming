# 13. Write a Python program to check if a character entered by the user is an alphabet or
#     not. If the user enters more than one character as input, the program prints some
#     appropriate error message and exit.

a=str(input("Enter any character: "))

if len(a) > 1:
    print("Please enter only one character")
elif ('a' <= a <= 'z' or 'A' <= a <= 'Z'):
    print("This Character is a Alphabet")
else:
    print("This Character is not a Alphabet")

        
