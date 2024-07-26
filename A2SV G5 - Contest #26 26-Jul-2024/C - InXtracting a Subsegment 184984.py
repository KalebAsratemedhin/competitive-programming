# Problem: C - InXtracting a Subsegment - https://codeforces.com/gym/537362/problem/C

n, k = map(int, input().split())
arr = list(map(int, input().split()))
if k == 1:
    print(min(arr))
elif k == 2:
    print(max(arr[0], arr[-1]))
else:
    print(max(arr))

