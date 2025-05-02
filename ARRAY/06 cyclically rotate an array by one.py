#naive
def cyclically_rotate(arr):
    if len(arr) <= 1:
        return arr
    last = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        arr[i + 1] = arr[i]
    arr[0] = last
    return arr
