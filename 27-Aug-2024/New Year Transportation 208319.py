# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())

arr = list(map(int, input().split()))

pos = 1

while pos <= n:
    if pos == t:
        print("YES")
        break
    elif pos > t:
        print("NO")
        break

    pos += arr[pos - 1]

