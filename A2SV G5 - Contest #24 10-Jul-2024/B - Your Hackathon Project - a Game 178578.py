# Problem: B - Your Hackathon Project - a Game - https://codeforces.com/gym/534160/problem/B

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for i in range(n)]
suffix = [0 for i in range(n)]



for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        prefix[i] = prefix[i - 1] + (arr[i - 1] - arr[i])
    
    else:
        prefix[i] = prefix[i - 1] 

    if arr[n - 1 - i] < arr[n - i]:
        suffix[n - 1 - i] = suffix[n - i] + (arr[n - i] - arr[n - 1 - i])
    else:
        suffix[n - 1 - i] = suffix[n - i]


for _ in range(m):
    s, t = map(int, input().split())
    if s < t:
        print(prefix[t - 1] - prefix[s - 1])
    else:
        print(suffix[t - 1] - suffix[s - 1])
   
