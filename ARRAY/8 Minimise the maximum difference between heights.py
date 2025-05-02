#greedy (with bubble sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def minimize_max_difference(arr, k):
    n = len(arr)
    if n <= 1:
        return 0
    bubble_sort(arr)
    result = arr[-1] - arr[0]
    smallest = arr[0] + k
    largest = arr[-1] - k
    for i in range(1, n):
        if arr[i] < k:
            continue
        min_curr = min(smallest, arr[i] - k)
        max_curr = max(largest, arr[i - 1] + k)
        result = min(result, max_curr - min_curr)
    return result
