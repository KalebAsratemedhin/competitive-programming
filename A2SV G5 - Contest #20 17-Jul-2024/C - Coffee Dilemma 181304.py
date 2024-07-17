# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C


import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []
total = 0

for num in arr:
    total += num
    heapq.heappush(heap, num)

    while total < 0:
        total -= heapq.heappop(heap)

print(len(heap))
