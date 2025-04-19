# 7. Write a program to Find the factorial of a given number.

n1=int(input('Enter any number: '))

a=1
for n in range(n1,1,-1):
   a*=n
print("Factorial of ",n1," is: ",a)
