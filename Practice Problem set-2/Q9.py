# 9. Write a Python program to guess a number between 1 and 9.
#    Note : User is prompted to enter a guess. If the user guesses wrong then the prompt
#    appears again until the guess is correct, on successful guess, user will get a "Well
#    guessed!" message, and the program will exit.

import random


n2=random.randint(1, 9)
n1=int(input('Enter a guess: '))

while(n1!=n2):
    print("Wrong guess. Try again.")
    n1=int(input('Enter a guess: '))
    
print("Well guessed!")
