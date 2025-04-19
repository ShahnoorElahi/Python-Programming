# 10. Write a Python function to create and print a list where the values
#     are the squares of numbers between 1 and 30.


def cList():
      L=[]
      for i in range(1,31):
        L.append(i**2)
      return L


print(cList())


