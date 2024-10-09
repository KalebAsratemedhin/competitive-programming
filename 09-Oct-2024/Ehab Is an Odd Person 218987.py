# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
arr = list(map(int, input().split()))

even = odd = 0
for num in arr:
    if num & 1:
        odd += 1
    else:
        even += 1
    

if even and odd:
    arr.sort()


for a in arr:
    print(a, end=" ")

