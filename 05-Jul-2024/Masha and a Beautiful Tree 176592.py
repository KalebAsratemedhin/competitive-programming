# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())

def merge(left, right, steps):
    if left == -1 or right == -1:
        return [-1, steps]
    
    if left[-1] <= right[0]:
        return [left + right, steps]
    elif right[-1] <= left[0]:
        return [right + left, steps + 1]
    else:
        return [-1, steps]

def mergeSort(arr, steps):
    if len(arr) <= 1:
        return [arr, steps]
    if arr == -1:
        return [arr, steps]
    
    mid = len(arr) // 2
    
    left = mergeSort(arr[:mid], 0)
    right = mergeSort(arr[mid:], 0)
    return merge(left[0], right[0], left[1] + right[1] + steps)

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = mergeSort(arr,0)
    if ans[0] == -1:
        print(ans[0])
    else:
        print(ans[1])
    
    