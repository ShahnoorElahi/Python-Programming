# 14. Write a Python function to sum all the numbers in a list using
#     recursion.

a = [1,1,1]
def sumOfList(n):

    if n < 0:
        return 0
    elif n==0:
        return a[0]
    else:
        return a[n] + sumOfList(n - 1)
    
    



print("Sum of all the numbers in a list = ",a," is:")
print(sumOfList(len(a)-1))



