# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq
n = int(input())

heap = []

ans = []
for _ in range(n):
    record = input().split()
    if len(record) == 2:
        op, num = record[0], int(record[1])
        if op == "insert":
            heapq.heappush(heap, num)
            ans.append(" ".join(record))
        else:
            if heap:
                
                
                while heap and heap[0] < num:
                    ans.append("removeMin")
                    heapq.heappop(heap)
                
                if heap and heap[0] == num:
                    ans.append(" ".join(record))
                else:
                    ans.append(f"insert {num}") 
                    heapq.heappush(heap, num)
                    ans.append(" ".join(record))
            else:
                ans.append(f"insert {num}") 
                heapq.heappush(heap, num)
                ans.append(" ".join(record))


    else:
        if heap:
            heapq.heappop(heap)
            ans.append(record[0])
        else:
            ans.append("insert 1") 
            ans.append(record[0])

print(len(ans))
for a in ans:
    print(a)

