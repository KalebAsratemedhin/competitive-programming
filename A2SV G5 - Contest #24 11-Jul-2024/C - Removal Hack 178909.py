# Problem: C - Removal Hack - https://codeforces.com/gym/534160/problem/C

n = int(input())
children = [1 for i in range(n + 1)]
disres = []
ans = []
for i in range(n):
    p, c = map(int, input().split())
    if p != -1:
        children[p] *= c
    if c:
        disres.append(i + 1)


disres.sort()

for node in disres:
    if children[node]:
        ans.append(str(node))

if not ans:
    print(-1)
else:
    print(" ".join(ans))


