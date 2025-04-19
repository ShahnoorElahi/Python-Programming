marksObtain=int(input('Enter total Marks Obtain: '))
totalMarks=int(input('Enter total Marks: '))
percentage=marksObtain/totalMarks*100

if(percentage > 90):
    print("A Grade")
elif(percentage > 75):
    print("B Grade")
elif(percentage > 65):
    print("C Grade")
