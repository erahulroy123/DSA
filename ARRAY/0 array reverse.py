#naive approach
def reverseArray(arr):
    n = len(arr)
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[n - i - 1]
    for i in range(n):
        arr[i] = temp[i]
arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")

#two pointer approach
def array_reverse(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
arr = [1, 4, 3, 2, 6, 5]
array_reverse(arr)
print(arr)

#recurssion
def array_reverse(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    array_reverse(arr, left + 1, right - 1)
arr = [1, 4, 3, 2, 6, 5]
array_reverse(arr, 0, len(arr) - 1)
print(arr)
