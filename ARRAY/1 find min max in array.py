#linear search
def find_max_min(arr):
    if len(arr) == 0:
        return None, None
    max_val = min_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val
arr = [1, 4, 3, 2, 6, 5]
max_val, min_val = find_max_min(arr)

#Divide and conquer
def find_max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    mid = (low + high) // 2
    left_max, left_min = find_max_min(arr, low, mid)
    right_max, right_min = find_max_min(arr, mid + 1, high)
    return max(left_max, right_max), min(left_min, right_min)
arr = [1, 4, 3, 2, 6, 5]
max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
