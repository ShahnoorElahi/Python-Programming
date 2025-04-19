#18. Find the sum of squares of each element of the list
#    using for loop. numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]

a=[3, 5, 23, 6, 5, 1, 2, 9, 8]

sum_of_square=0

for i in range(0,len(a)):
        sum_of_square+=a[i]**2
  
print("Sum_of_Square: ",sum_of_square)

    
