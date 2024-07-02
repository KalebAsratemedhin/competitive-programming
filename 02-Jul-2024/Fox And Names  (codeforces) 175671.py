# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque


n = int(input())
succeeding = {chr(ord('a') + i) : [] for i in range(26)}
indegrees = {chr(ord('a') + i) : 0 for i in range(26)}
impossible = False
arr = []
for _ in range(n):
    arr.append(input())

for i in range(n - 1):
    curr = arr[i]
    nxt = arr[i + 1]
    i = 0
    
    
    while i < min(len(curr), len(nxt)) and curr[i] == nxt[i]:
        i += 1
    
    if i <  min(len(curr), len(nxt)):
        succeeding[curr[i]].append(nxt[i])
        indegrees[nxt[i]] += 1
    elif len(nxt) < len(curr):
        impossible = True
        break

if impossible:
    print("Impossible")
else:
    start = arr[0][0]
    queue = deque()


    for key, value in indegrees.items():
        if value == 0:
            queue.append(key)

    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node)

        for adj in succeeding[node]:
            indegrees[adj] -= 1
            if indegrees[adj] == 0:
                queue.append(adj)



    ans = "".join(ans)

    if len(ans) < 26:
        print("Impossible")
    else:
        print(ans)


    

