import sys

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

def check_conjecture(n):
    for p in range(3, n//2+1):
        if primes[p] == 1 and primes[n-p] == 1:
            return str(n)+' = '+str(p)+' + '+str(n-p)
            break
    return "Goldbach's conjecture is wrong."

n = int(sys.stdin.readline())
while n != 0:
    print(check_conjecture(n))
    n = int(sys.stdin.readline())
