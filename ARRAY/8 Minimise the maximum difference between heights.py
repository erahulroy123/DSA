#greedy
def minimize_max_difference(arr, k):
    n = len(arr)
    if n == 1:
        return 0
    arr.sort()
    min_height = arr[0] + k
    max_height = arr[-1] - k
    result = arr[-1] - arr[0]
    for i in range(1, n):
        if arr[i] < k:
            continue
        min_curr = min(min_height, arr[i] - k)
        max_curr = max(max_height, arr[i - 1] + k)
        result = min(result, max_curr - min_curr)
    return result
