#17. Write a Python program to count the number of even
#    and odd numbers from a series of numbers.
#    Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
evenCount=0
oddCount=0

for i in range(0,len(a)):
        if a[i]%2==0:
                evenCount+=1
        else:
                oddCount+=1
  
print("OddCount: ",oddCount)
print("EvenCount: ",evenCount)
    
