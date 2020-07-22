def bubble_sort(array):
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j]> array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
array=[]
n=int(input("enter the size of the array"))
for i in range(n):
    elements=int(input("enter the element"))
    array.append(elements)
print("sorted array")
bubble_sort(array)
for i in range(n):
    print(array[i])
