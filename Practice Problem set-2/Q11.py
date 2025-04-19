# 11. Write a Python program that accepts a string and calculates
#     the number of digits and letters.
#     Sample Data : Python 3.2
#     Expected Output :
#     Letters 6
#     Digits 2.


w1=str(input('Enter a string: '))

a=len(w1)-1
wCount=0
dCount=0
while(a>=0):
    if ('a'<=w1[a]<='z' or 'A'<=w1[a]<='Z'):
        wCount+=1
    elif ('0'<=w1[a]<='9'):
        dCount+=1
    a-=1

print(wCount,dCount)
    
