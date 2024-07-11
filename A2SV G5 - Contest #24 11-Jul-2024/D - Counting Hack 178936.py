# Problem: D - Counting Hack - https://codeforces.com/gym/534160/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    left_index, right_index = [], []
    left_set, right_set = set(), set()

    for i in range(n):
        if arr[i] not in left_set:
            left_set.add(arr[i])
            left_index.append(i)
    
    for i in range(n - 1, -1, -1):
        if arr[i] not in right_set:
            right_set.add(arr[i])
            right_index.append(i)

    right_index = right_index[::-1]

    ans, right = 0, 0

    for left in left_index:
        while right < len(right_index) and right_index[right] < left:
            right += 1
        ans += len(right_index) - right

    print(ans)