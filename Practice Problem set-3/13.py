# 13. Write a python function to Find Factorial of Number Using
#     Recursion.


def Factorial(n):
    
    if n <= 0:
        return "undefine"
    elif n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


n = int(input("Enter the number of terms for the Fibonacci sequence: "))
print(Factorial(n))


