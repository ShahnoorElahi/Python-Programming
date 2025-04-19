# 2. Write a python function to sum all the numbers in a list

a=[1,2,3]

def SumOfAllNumbers():
    totalSum=a[0]
    for i in range(1,len(a)):
        totalSum+=a[i]
    return totalSum

print("Sum of all the numbers in a list: ",SumOfAllNumbers())
