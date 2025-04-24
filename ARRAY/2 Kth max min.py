#selection sort
def kth_min_max_manual_sort(arr, k):
    n = len(arr)
    if k < 1 or k > n:
        return None, None
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    kth_min = arr[k - 1]
    kth_max = arr[n - k]
    return kth_min, kth_max
arr = [7, 10, 4, 3, 20, 15]
k = 3
kth_min, kth_max = kth_min_max_manual_sort(arr, k)

#
