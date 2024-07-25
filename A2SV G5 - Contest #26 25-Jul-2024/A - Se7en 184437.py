# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 7 == 0:
        print(n)
    
    else:
        rem = n % 7
        d = str(n)
        if int(d[-1]) - rem >= 0:
            print(n - rem)
        else:
            print(n + (7 - rem))



