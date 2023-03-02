# 런타임 에러
import sys

n = int(sys.stdin.readline())

def find_primes(n): #에라토스테네스의 체
    array = [1 for _ in range(n+1)]
    for i in range(2, int(n ** 0.5) + 1):
        if array[i]:
            j = 2
        while i * j <= n: # 배수 모두 제거
            array[i * j] = 0
            j += 1
    return array

primes = find_primes(1000000)

for _ in range(n):
    x = int(sys.stdin.readline())
    result = 0
    for p in range(2,x//2+1):
        if primes[p] == 1 and primes[x-p] == 1:
            result += 1
    print(result)