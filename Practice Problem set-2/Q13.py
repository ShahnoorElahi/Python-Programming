# 13. Write a Python program to print the number of vowels and consonant in your full
#     name.


w1=str(input('Enter your Full Name: '))

vCount=0
cCount=0
vowels="aeiouAEIOU"

for i in w1:
        if i in vowels:
            vCount+=1
        elif ('a'<=i<='z'  or  'A'<=i<='Z'):
            cCount+=1
print("Total Vowels: ",vCount,"Total Consonants: ",cCount)
    
