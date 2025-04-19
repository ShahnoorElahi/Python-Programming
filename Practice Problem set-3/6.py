# 6. Write a Python function that takes a list and returns a new list with
#    distinct elements from the first list.



def uniqueList(iList):
    uList=[]
    for element in iList:
        if element not in uList:
            uList.append(element)
    return uList


iList=[1, 2, 2, 3, '4',4, '4', 5]


print("UniqueList: ",uniqueList(iList))
