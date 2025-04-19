# 6. Write a program to display all prime numbers within a range.

n1=int(input('Enter first number of range: '))
n2=int(input('Enter last number of range: '))


for n in range(n1,n2+1):
    flag=0
    for i in range(2, int(n*0.5)+1):
        if ((n%i) == 0):
            flag=1
            break
    if (flag == 0 and n > 1):
        print(n)
