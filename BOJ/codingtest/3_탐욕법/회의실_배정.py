import sys

input = sys.stdin.readline

n = int(input())
d = []
for _ in range(n):
    s, e = map(int, input().split())
    d.append([e, s])

d.sort()
t = 0
result = 0
for e, s in d:
    if t <= s:
        t = e # s=e, e 이후로 사용할 수 있게 시작 t가 변경 되야함
        result += 1
print(result)