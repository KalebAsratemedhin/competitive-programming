# Problem: A - The Coordinate Challenge - https://codeforces.com/gym/531455/problem/A


t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(2)
    elif n % 3 == 0:
        print(n // 3)
    elif n % 3 == 1:
        if n >= 4:
            print ((n - 4) // 3 + 2  )
        else:
            print ((n - 2) // 3 + 1  ) 
    else:
        if n >= 2:
            print ((n - 2) // 3 + 1  )
        else:
            print ((n - 2) // 3 + 1  )