# 12. Write a python function to display Fibonacci Sequence Using
#     Recursion.


def fibonacci(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def display_fibonacci_sequence(terms):
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:")
        for i in range(terms):
            print(fibonacci(i), end=" ")


terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
display_fibonacci_sequence(terms)


