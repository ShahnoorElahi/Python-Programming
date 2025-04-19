# 7. Write a Python function that takes a number as a parameter and
#    checks whether the number is prime or not.



def isPrime(n):
    flag=0
    for i in range(2, int(n*0.5)+1):
        if ((n%i) == 0):
            print("number is Composite(not prime)")
            flag=1
            break
    if (flag == 0):
        print("number is prime")
    


n=int(input('Enter any number: '))

isPrime(n)
