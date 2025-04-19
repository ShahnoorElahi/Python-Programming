# 10. Write a Python program that accepts a word from the user and reverses it.


w1=str(input('Enter a word: '))

a=len(w1)-1
b=""
while(a>=0):
    b+=w1[a]
    a-=1
w1=b
print(w1.rsort())
    
