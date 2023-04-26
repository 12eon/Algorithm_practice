import sys

n = int(input())
k = int(input())

if k >= n:
    print(0)
else:
    num = list(map(int, input().split(' ')))
    num.sort()

    distances = []
    for i in range(1, n):
        distances.append(num[i] - num[i - 1])
    distances.sort(reverse=True)

    for i in range(k - 1):
        distances[i] = 0

    print(sum(distances))