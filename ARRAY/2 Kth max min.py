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

#min/max heap
import heapq

def kth_min_max_heap(arr, k):
    n = len(arr)
    if k < 1 or k > n:
        return None, None
    min_heap = arr.copy()
    heapq.heapify(min_heap)
    kth_min = None
    for _ in range(k):
        kth_min = heapq.heappop(min_heap)
    max_heap = [-num for num in arr]
    heapq.heapify(max_heap)
    kth_max = None
    for _ in range(k):
        kth_max = -heapq.heappop(max_heap)
    return kth_min, kth_max
arr = [7, 10, 4, 3, 20, 15]
k = 3
kth_min, kth_max = kth_min_max_heap(arr, k)

#quick select
def quick_select(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index > k - 1:
            return quick_select(arr, low, pivot_index - 1, k)
        else:
            return quick_select(arr, pivot_index + 1, high, k)
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
def kth_min_max_quick_select(arr, k):
    n = len(arr)
    if k < 1 or k > n:
        return None, None
    kth_min = quick_select(arr.copy(), 0, n - 1, k)
    kth_max = quick_select(arr.copy(), 0, n - 1, n - k + 1)
    return kth_min, kth_max
arr = [7, 10, 4, 3, 20, 15]
k = 3
kth_min, kth_max = kth_min_max_quick_select(arr, k)
