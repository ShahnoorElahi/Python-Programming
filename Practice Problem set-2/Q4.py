# 4. Write a program to display only those numbers from a list (numbers = [12, 75, 150,
#    180, 145, 525, 50]) that satisfy the following conditions:
#    The number must be divisible by five
#    If the number is greater than 150, then skip it and move to the next number
#    If the number is greater than 500, then stop the loop

a=[12, 75, 150, 180, 145, 525, 50]

for i in range(0,len(a)):
    if a[i]%5==0:
        if a[i] < 501 :
            if a[i] < 151:
                print(a[i])
        else:
            break
