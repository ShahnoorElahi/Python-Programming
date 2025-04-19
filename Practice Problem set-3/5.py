# 5. Write a Python function that accepts a string and counts the number
#    of upper- and lower-case letters.



def upperCaseCount(a):
    uCount=0
    for i in a:
        if 'A'<=i<='Z':
            uCount+=1
    return uCount

def lowerCaseCount(a):
    lCount=0
    for i in a:
        if 'a'<=i<='z':
            lCount+=1
    return lCount

a=str(input("Enter any string: "))

print("Upper-case letters: ",upperCaseCount(a))
print("Lower-case letters: ",lowerCaseCount(a))
