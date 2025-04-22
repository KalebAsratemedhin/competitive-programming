MAX_NUM = 10 ** 4 + 10
MAX_PRIME_POWER = 15

MOD = 10 ** 9 + 7

sieve = [0] * MAX_NUM

for num in range(2, MAX_NUM):
    if sieve[num] == 0:
        for multiple in range(num, MAX_NUM, num):
            sieve[multiple] = num

primes = [[] for i in range(MAX_NUM)]

for num in range(2, MAX_NUM):
    curr = num
    while curr > 1:
        prime = sieve[curr]

        count = 0
        while curr % prime == 0:
            count += 1
            curr //= prime
        
        primes[num].append(count)

combinations = [ [0] * MAX_PRIME_POWER for i in range(MAX_NUM + MAX_PRIME_POWER)]

combinations[0][0] = 1

for buckets in range(1, MAX_NUM + MAX_PRIME_POWER):
    combinations[buckets][0] = 1
    for power in range(1, MAX_PRIME_POWER):
        combinations[buckets][power] = (combinations[buckets - 1][power] + combinations[buckets - 1][power - 1]) % MOD



class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for m in range(1, maxValue + 1):
            temp = 1
            for prime in primes[m]:
                temp *= combinations[n + prime - 1][prime]
            
            ans = (ans + temp) % MOD

        return ans
        