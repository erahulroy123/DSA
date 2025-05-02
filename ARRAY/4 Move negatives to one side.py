#two pointers
def move_negatives(arr):
    low, high = 0, len(arr) - 1 
    while low <= high:
        if arr[low] < 0 and arr[high] >= 0:
            low += 1
            high -= 1
        elif arr[low] >= 0 and arr[high] < 0:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
        elif arr[low] >= 0:
            low += 1
        else:
            high -= 1      
    return arr
