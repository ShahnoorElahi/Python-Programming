# 11. Write a program that takes password from user as input. Validate the password on the
#     following criteria:
#     Password length between 7 to 15 characters which contain at least one numeric digit
#     and a special character is acceptable.
a = input("a= ")
if (str(1) in a) or (str(2) in a) or (str(3) in a) or (str(4) in a) or (str(5) in a) or (str(6) in a) or (str(7) in a) or (str(8) in a) or (str(9) in a) or (str(0) in a):
    if (str('`') in a) or (str('~') in a) or (str('!') in a) or (str('@') in a) or (str('#') in a) or (str('$') in a) or (str('%') in a) or (str('^') in a) or (str('&') in a) or (str('*') in a) or (str('(') in a) or (str(')') in a) or (str('-') in a) or (str('_') in a) or (str('+') in a) or (str('=') in a) or (str('[') in a) or (str(']') in a) or (str('{') in a) or (str('}') in a) or (str('|') in a) or (str('\\') in a) or (str('/') in a) or (str(':') in a) or (str(';') in a) or (str('\'') in a) or (str('"') in a) or (str('<') in a) or (str('>') in a) or (str(',') in a) or (str('.') in a) or (str('?') in a):
        if (len(a)>=7) and (len(a)<=15):
            print("Password is valid")
        else:
            print("Password is invalid")
    else:
        print("Password is invalid")
else:
    print("Password is invalid")












# second method

a = input("a= ")
flag=0
if (7<=len(a)<=15):
    if a.isascii():
        for i in "1234567890":
            if i in a:
                print('v')
                flag=1
                break
        if flag==0:
            print('iv')
    else:
        print('iv')
else:
    print('iv')
