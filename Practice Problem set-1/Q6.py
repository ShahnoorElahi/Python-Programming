#6. Write a program to print lowest number from the two values provided by the user.

n1=int(input('Enter any number_1: '))
n2=int(input('Enter any number_2: '))
if (n1>n2):
    print(n2," is the lowest number")
elif (n1==n2):
    print("Both numbers are equal to each other")
else:
    print(n1," is the lowest number")

