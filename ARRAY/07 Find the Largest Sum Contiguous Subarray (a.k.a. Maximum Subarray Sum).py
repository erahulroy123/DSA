#sliding window
def max_sum_subarray(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

#dynamic Programming(Kadane's algorithm)
def max_subarray_sum(arr):
    max_sum = arr[0] 
    current_sum = arr[0]  
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
