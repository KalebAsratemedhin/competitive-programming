# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
 
def _min(m, s):
    first = max(s - 9 * (m - 1), 1)
    s -= first
    ans_min = [None] * m
    ans_min[0] = str(first)
    for i in range(m - 1, 0, -1):
        cur = min(9, s)
        s -= cur
        ans_min[i] = str(cur)
    return ''.join(ans_min)
    
def _max(m, s):
    ans = [None] * m
    for i in range(m):
        cur = min(9, s)
        s -= cur
        ans[i] = str(cur)
    return ''.join(ans)
 
if s == 0:
    if m == 1:
        print(0, 0)
    else:   
        print(-1, -1)
        
elif m * 9 < s:
    print(-1, -1)
 
else:
    print(_min(m, s), _max(m, s))