# 1. write a python function to find the maximum of three numbers

a=[1,4,3]

def largestNumber():
    maxNum=a[0]
    for i in range(1,len(a)):
        if a[i]>maxNum:
            maxNum=a[i]
    return maxNum

print("Maximum of three numbers is: ",largestNumber())
