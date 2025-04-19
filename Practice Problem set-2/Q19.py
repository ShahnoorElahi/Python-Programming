# 19. From given list: gadgets = [“Mobile”, “Laptop”, 100, “Camera”,
#     310.28, “Speakers”, 27.00, “Television”, 1000, “Laptop Case”,
#     “Camera Lens”]
#a) Create separate lists of strings and numbers.
#b) Sort the strings list in ascending order
#c) Sort the strings list in descending order
#d) Sort the number list from lowest to highest
#e) Sort the number list from highest to lowest

gadgets = ['Mobile', 'Laptop', 100, 'Camera',310.28, 'Speakers',
           27.00, 'Television', 1000, 'Laptop Cas', 'Camera Lens']

str_Values=[]
num_Values=[]

for i in range(0,len(gadgets)):
        if(type(gadgets[i])==str):
                str_Values.append(gadgets[i])
        else:
                num_Values.append(gadgets[i])
  
print("String Values: ",str_Values)
print("Number Values: ",num_Values)
print("String Values in Descending Order: ",sorted(str_Values,reverse=True))
print("String Values in Ascending Order: ",sorted(str_Values))
print("Number Values in Ascending Order: ",sorted(num_Values))
print("Number Values in Descending Order: ",sorted(num_Values,reverse=True))

    
