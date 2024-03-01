t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    prefix = 0
    count = 0
    dict = {}
    for i in range(n + 1):
        if prefix - i in dict:
            count += dict[prefix - i]
        dict[prefix - i] = dict.get(prefix - i, 0) + 1
        if i < n:
            prefix += int(s[i])
        
    print(count)