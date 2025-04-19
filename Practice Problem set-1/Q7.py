#7. Write a program to check if the character entered by user is vowel or consonant.

character=str(input('Enter any number_1: '))
vowels="AEIOUaeiou"
flag=0
for i in vowels:
    if (character == i):
        print(character," is a vowel")
        flag=1
        break
if (flag==0):
   print(character," is a consonant(not vowel)")

