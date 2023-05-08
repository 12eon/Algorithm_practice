# 숫자 카드 게임 : 각 행마다 가장 작은 숫자 -> 가장 큰 숫자

n,m = map(int, input().split())
value = []
for _ in range(n):
    value.append(list(map(int, input().split())))

result = 0
for i in range(n):
    cmp = min(value[i]) # sort < min : 필요한 부분만 탐색
    if result < cmp:
        result = cmp

print(result)