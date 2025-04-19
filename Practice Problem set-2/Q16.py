# 16. Write a python program to select the maximum value from list
#     (without using maximum function).

a=[1,2,3,2,1,4,9,4,2,1]
max_value=a[0]

for i in range(1,len(a)):
        if a[i]>max_value:
                max_value=a[i]
  
print("Maximum Value: ",max_value)
    
