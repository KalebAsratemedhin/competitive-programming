# Problem: D - A Tree that Needs Addis Hiwot - https://codeforces.com/gym/537362/problem/D

from heapq import heapify, heappop, heappush
from sys import stdin


def input(): return stdin.readline().strip()


t = int(input())
for _ in range(t):
    n = int(input())
    parent = list(map(int,input().split()))
    
    children = [[] for i in range(n)]
    for i in range(n -1):
        children[parent[i] - 1].append(i + 1)
    
    children.sort(key = lambda x : len(x),reverse=True)
    

    arr = []

    for i in children:
        if len(i) != 0:
            arr.append(len(i))
    
    arr.append(1)
    
    for i in range(len(arr)):
        arr[i] += i
        
    if max(arr) == arr[-1]:
        print(arr[-1])
        
    else:
        
        cur_ans = arr[-1]
        for i in range(len(arr)):
            arr[i] = -arr[i]
            
        heapify(arr)
        
        while cur_ans < -arr[0]:
            cur = heappop(arr)
            heappush(arr,cur + 1)
            cur_ans += 1
            
        print(cur_ans) 