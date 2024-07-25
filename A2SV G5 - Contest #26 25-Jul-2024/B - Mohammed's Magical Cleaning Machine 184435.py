# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

t = int(input())


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ops = 0
    pointer = 0

    for i in range(n - 1):
        
        if not arr[i]:
            if arr[pointer] > 0:
                arr[i] += 1
                ops += 1
                arr[pointer] -= 1
            if not arr[pointer]:
                pointer += 1
            
    
    print(ops + sum(arr[:-1]))

