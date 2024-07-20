# Problem: E - Finding a Path - https://codeforces.com/gym/530187/problem/E

from collections import defaultdict

def solve():

    n, a, b = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(n - 1):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    pref1 = [-1] * (n + 1)
    pref1[a] = 0
    stack = [(a, -1)]
    
    while stack:
        node, par = stack.pop()

        for neighbour, weight in graph[node]:
            if neighbour != par:
                if neighbour == b:
                    if weight ^ pref1[node] == 0:
                        return "YES"
                    continue
                
                pref1[neighbour] = weight ^ pref1[node]
                stack.append((neighbour, node))
                
    prefix_set = set(pref1)
    pref2 = [-1] * (n + 1)
    pref2[b] = 0
    stack = [(b, -1)]
    
    while stack:

        node, par = stack.pop()
        for neighbour, weight in graph[node]:
            if neighbour != par:

                pref2[neighbour] = weight ^ pref2[node]
                if pref2[neighbour] in prefix_set:
                    return "YES"
                
                stack.append((neighbour, node))
  
    return "NO"

t = int(input())
for _ in range(t):
    print(solve())

