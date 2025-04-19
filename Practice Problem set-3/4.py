# 4. Write a Python function to check whether a number falls within a
#    given range.



def NumberInRange(a,b,c):
    if b<=a<=c:
        return "Number falls within a given range."
    else:
        return "Number falls out of a given range."

a=int(input("Enter any number: "))
b=int(input("Enter Starting number of range: "))
c=int(input("Enter Ending number of range: "))

print(NumberInRange(a,b,c))
