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

#two pointer
def find_max_min_two_pointer(arr):
    if not arr:
        return None, None
    left, right = 0, len(arr) - 1
    max_val = arr[left]
    min_val = arr[left]
    while left <= right:
        if arr[left] > max_val:
            max_val = arr[left]
        if arr[left] < min_val:
            min_val = arr[left]  
        if arr[right] > max_val:
            max_val = arr[right]
        if arr[right] < min_val:
            min_val = arr[right]
        left += 1
        right -= 1
    return max_val, min_val
