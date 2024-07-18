# Problem: C - The Alchemist - https://codeforces.com/gym/530187/problem/C

from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    free = set(map(int, input().split()))

    adjacents = defaultdict(list)
    degree = [0] * (n + 1)
    future = [0] * (n + 1)
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        m, edges = line[0], line[1:]
        if i in free:
            continue

        degree[i] = m
        for a in edges:
            adjacents[a].append(i)
    
    queue = deque()
    for node in range(1, n + 1):
        if node in free:
            queue.append(node)
        elif degree[node] == 0:
            ans[node] = cost[node]
            queue.append(node)

    while queue:
        node = queue.popleft()
        for child in adjacents[node]:
            degree[child] -= 1
            future[child] += ans[node]
            if degree[child] == 0:
                queue.append(child)
                ans[child] = min(cost[child], future[child])

    print(*ans[1:])
