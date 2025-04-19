#9. Write a program that solves quadratic equation and prints the output only if the roots
#   are real.


a=int(input('Enter a: Coefficient of x^2: '))
if a == 0:
        print("Not a quadratic equation")
else:
    b=int(input('Enter b: Coefficient of x: '))
    c=int(input('Enter c: Constant term.: '))


    delta = (b**2) - 4*(a*c)
    if (delta >= 0):  
        root1 = (-b - delta**0.5) / (2*a)
        root2 = (-b + delta**0.5) / (2*a)
        print("The roots are real: ",root1," ",root2)
    elif (delta < 0):
        print("The roots are complex")
        
        
