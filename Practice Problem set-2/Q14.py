# 14. Write a Python program that generates list of values. The
#     values must be taken from user as input.

a=str(input('Enter Value (Enter exit to stop): '))
w1=[]
while(a != 'exit'):
        w1.append(a)
        a=str(input('Enter Value (Enter exit to stop)'))
  
print("All Values: ",w1)
    
