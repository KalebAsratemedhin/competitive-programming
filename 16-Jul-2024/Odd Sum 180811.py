# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

pos_odd = []
neg_odd = []
even_sum = 0


for num in arr:
    if num & 1:
        if num > 0:
            pos_odd.append(num)
        elif num < 0:
            neg_odd.append(num)

    elif num > 0:
        even_sum += num
    

if len(pos_odd) % 2:
    print(even_sum + sum(pos_odd))
elif len(pos_odd) > 0:
    diff = pos_odd.pop()
    ans = even_sum + sum(pos_odd)

    if len(neg_odd):
        evn = diff + neg_odd[0]
        if evn > 0:
            ans += evn
    print(ans)

elif neg_odd:
    print(even_sum + neg_odd[0])






