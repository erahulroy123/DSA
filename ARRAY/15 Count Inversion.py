#modified binary search
def getInversions(arr, n):
    sorted_unique = sorted(set(arr))
    ranks = {val: i+1 for i, val in enumerate(sorted_unique)}
    bit = [0] * (len(ranks) + 1)
    def update(bit, index, value):
        while index < len(bit):
            bit[index] += value
            index += index & -index 
    def query(bit, index):
        result = 0
        while index > 0:
            result += bit[index]
            index -= index & -index
        return result
    inversions = 0
    for num in reversed(arr):
        rank = ranks[num]
        inversions += query(bit, rank - 1)
        update(bit, rank, 1)  
    return inversions
