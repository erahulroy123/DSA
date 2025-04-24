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
print(f"Maximum: {max_val}, Minimum: {min_val}")
