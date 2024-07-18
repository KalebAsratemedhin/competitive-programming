# Problem: D - Max of Max - https://codeforces.com/gym/530187/problem/D

def check(max_val):

    for i in range(n):

        cost = 0
        curr = max_val
        for j in range(i, n):
            if a[j] < curr and j == n - 1:
                cost = k + 1
                break
            
            if a[j] >= curr:
                break

            cost += curr - a[j]
            next = max(curr - 1, 0)
            curr = next

        if cost <= k:
            return True

    return False



t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    low = max(a)
    high = max(a) + min(k, n)

    while low <= high:

        mid = low + (high - low)//2

        if check(mid):
            low = mid + 1
        
        else:
            high = mid - 1
    
    print(high)