#8. Write a program that takes the dimensions (length of sides) of triangle to identify if
#   the triangle is right angle triangle.

side=[]
side.append(int(input('Enter length of side_1: ')))
side.append(int(input('Enter length of side_2: ')))
side.append(int(input('Enter length of side_3: ')))

side=sorted(side)
if(side[0]**2+side[1]**2==side[2]**2):
    print("it is a right angle triangle")
else:
    print("it is not a right angle triangle")
