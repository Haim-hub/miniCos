array = [1,8,3,9,2,10,4,6,7,5]
length = len(array)

def bubblesort(array):
    for i in range(length-1):
        for j in range(0,length-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
bubblesort(array)

for i in range(0, len(array)):
    print(array[i])