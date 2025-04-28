#dutch national flag algorithm
def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr
arr = [0, 1, 2, 1, 0, 2, 1, 0, 2]
sorted_arr = sort_012(arr)

#count sort
def sort_012_count(arr):
    count = [0, 0, 0] 
    for num in arr:
        count[num] += 1
    index = 0
    for i in range(3):
        for j in range(count[i]):
            arr[index] = i
            index += 1
    return arr
arr = [0, 1, 2, 1, 0, 2, 1, 0, 2]
sorted_arr = sort_012_count(arr)
