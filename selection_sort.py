array=[]
size=int(input("enter the size of the list"))
for i in range(size):
    elements=int(input("enter element"))
    array.append(elements)
for i in range(size):
    min = i
    for j in range(i+1 , size):
        if(array[min]>array[j]):
            min = j
    array[i] , array[min] = array[min] , array[i]
for i in range(size):
    print(array[i])
