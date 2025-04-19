# 14. Write a Python program that requests five integer values from the user. It then prints
#     one of two things: if any of the values entered are duplicates, it prints "DUPLICATES";
#     otherwise, it prints "ALL UNIQUE".

a=[]
a.append(int(input("Enter No_1: ")))
a.append(int(input("Enter No_2: ")))
a.append(int(input("Enter No_3: ")))
a.append(int(input("Enter No_4: ")))
a.append(int(input("Enter No_5: ")))


flag=0
for i in a:
    if a.count(i)>=2:
      print("DUPLICATES")
      flag==1
      break

if flag==0:
      print("ALL UNIQUE")










# second method

a=[]
a.append(int(input("Enter No_1: ")))
a.append(int(input("Enter No_2: ")))
a.append(int(input("Enter No_3: ")))
a.append(int(input("Enter No_4: ")))
a.append(int(input("Enter No_5: ")))




flag=0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            flag=1
            break
if flag==0:
      print("ALL UNIQUE")
else:
      print("DUPLICATES")
