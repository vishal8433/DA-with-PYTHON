def insertionsort(array):
    for i in range(1,len(array)):
        a=array[i]
        j=i-1
        while j>=0 and a<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=a
array=[]
size=int(input("\n enter the size of the list \t"))
for i in range(size):
    elements=(int(input("enter the element")))
    array.append(elements)
print("sorted list")
insertionsort(array)
for i in range(len(array)):
    print(array[i])
