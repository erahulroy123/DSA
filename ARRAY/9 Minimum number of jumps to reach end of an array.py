#greedy
def min_jumps_greedy(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    max_reach = arr[0]
    steps = arr[0]
    jumps = 1
    for i in range(1, n):
        if i == n - 1:
            return jumps
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i
    return -1

#bfs
from collections import deque
def min_jumps_bfs(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    queue = deque()
    queue.append((0, 0))
    visited = set()
    while queue:
        index, jumps = queue.popleft()
        max_jump = arr[index]
        for i in range(1, max_jump + 1):
            next_index = index + i
            if next_index >= n - 1:
                return jumps + 1
            if next_index not in visited:
                visited.add(next_index)
                queue.append((next_index, jumps + 1))
    return -1
