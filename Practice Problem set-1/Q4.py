#4. Write a program to check if number entered by user is prime or not.

n=int(input('Enter any number: '))

flag=0
for i in range(2, int(n*0.5)+1):
        if ((n%i) == 0):
            print("number is Composite(not prime)")
            flag=1
            break
if (flag == 0):
    print("number is prime")

































