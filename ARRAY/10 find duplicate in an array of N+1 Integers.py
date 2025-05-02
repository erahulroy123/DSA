#two Pointer(Floyd’s Cycle Detection)
def find_duplicate_floyd(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

#Modified Binary Search
def find_duplicate_binary_search(arr):
    low = 1
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        count = sum(num <= mid for num in arr)
        if count > mid:
            high = mid
        else:
            low = mid + 1
    return low
