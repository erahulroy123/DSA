#two pointers
def rearrange_negatives(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] < 0 and arr[right] >= 0:
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] < 0:
            left += 1
        else:
            right -= 1
    return arr
arr = [-1, 2, -3, 4, -5, 6]
rearranged_arr = rearrange_negatives(arr)

#partition logic (like quicksort)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
arr = [10, 80, 30, 90, 40, 50, 70]
low = 0
high = len(arr) - 1
pivot_index = partition(arr, low, high)
