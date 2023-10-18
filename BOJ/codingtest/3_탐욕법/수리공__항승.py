import sys

input = sys.stdin.readline

n, len = map(int, input().split())
len -= 1
p = list(map(int, input().split()))
p.sort()

result = 1 # 새로 선 추가
line = p[0]+len # 선 끝 위치
i = 1
while i < n:
    if p[i] > line:
        result += 1
        line = p[i]
    i += 1

print(result)