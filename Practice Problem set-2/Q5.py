# 5. Write a program to Print list in reverse order using a loop.

a=[12, 75, 150, 180, 145, 525, 50]

b=[]
for i in range(len(a) - 1, -1, -1):
    b.append(a[i])

print(b)
