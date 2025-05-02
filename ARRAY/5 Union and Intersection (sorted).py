#two pointer
def union_of_arrays(arr1, arr2):
    union = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1
    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    return union
def intersection_of_arrays(arr1, arr2):
    intersection = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            intersection.append(arr1[i])
            i += 1
            j += 1
    return intersection
