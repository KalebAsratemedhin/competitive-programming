# Problem: C - Yet Another Monocarp's Problem - https://codeforces.com/gym/532814/problem/C

def test(k, arr):
    total_damage = 0
    n = len(arr)
    
    for i in range(n - 1):
        interval = arr[i + 1] - arr[i]
        total_damage += min(interval, k)
    
    total_damage += k
    
    return total_damage

t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    attack_times = list(map(int, input().split()))
    
    low, high = 1, h

    while low < high:
        mid = (low + high) // 2
        if test(mid, attack_times) < h:
            low = mid + 1
        else:
            high = mid
    
    print(low)
