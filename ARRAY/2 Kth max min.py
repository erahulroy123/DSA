#top k elements
import heapq
def find_kth_max_min(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None, None
    max_kth = heapq.nlargest(k, arr)[-1] 
    min_kth = heapq.nsmallest(k, arr)[-1]
    return max_kth, min_kth

#modified binary search(quick select)
import random
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)
    return None
def find_kth_max_min(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None, None
    kth_min = quickselect(arr[:], 0, len(arr) - 1, k - 1)
    kth_max = quickselect(arr[:], 0, len(arr) - 1, len(arr) - k)
    return kth_max, kth_min
