#two pointer approach
def array_reverse(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
arr = [1, 2, 3, 4, 5]

#recurssion
def array_reverse(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    array_reverse(arr, left + 1, right - 1)
arr = [1, 2, 3, 4, 5]
