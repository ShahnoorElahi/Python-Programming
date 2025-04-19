# 3. Write a Python function to calculate the factorial of a number (a non-
#    negative integer). The function accepts the number as an argument.



def factorialOfNumber(a):
    if a<=0:
        return "I said, Please Enter a Positive number: "
    else:
        b=a
        for i in range(a-1,1,-1):
            b*=i
    return b


a=int(input("Enter any positive number: "))

print("Factorial Of Number: ",factorialOfNumber(a))
