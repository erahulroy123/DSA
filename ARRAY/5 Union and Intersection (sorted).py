#two pointer merge
def find_union_intersection(arr1, arr2):
    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    union_result = []
    intersection_result = []
    while i < n and j < m:
        if i > 0 and arr1[i] == arr1[i-1]:
            i += 1
            continue
        if j > 0 and arr2[j] == arr2[j-1]:
            j += 1
            continue
        if arr1[i] < arr2[j]:
            union_result.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            union_result.append(arr2[j])
            j += 1
        else:
            union_result.append(arr1[i])
            intersection_result.append(arr1[i])
            i += 1
            j += 1
    while i < n:
        if i == 0 or arr1[i] != arr1[i-1]:
            union_result.append(arr1[i])
        i += 1
    while j < m:
        if j == 0 or arr2[j] != arr2[j-1]:
            union_result.append(arr2[j])
        j += 1
    return union_result, intersection_result
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
union_result, intersection_result = find_union_intersection(arr1, arr2)

#using sets
def find_union_intersection_sets(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    union_result = list(set1 | set2)
    intersection_result = list(set1 & set2)
    union_result.sort()
    intersection_result.sort()
    return union_result, intersection_result
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
union_result, intersection_result = find_union_intersection_sets(arr1, arr2)
