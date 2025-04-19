# 12. Write a program to check if user has entered an upper-case character or lower-case
#     character (Use ‘ord’ function and ASCII codes).

a=str(input("Enter a Character: "))
    

if 65 <= ord(a) <= 90:  # ASCII range for uppercase letters (A-Z)
        print("Uppercase character")
elif 97 <= ord(a) <= 122:  # ASCII range for lowercase letters (a-z)
        print("Lowercase character")
else:
        print("This character is not an alphabet")
    
