# 절댓값을 고려하기 위해서 평균 이용
# 실패 - 시간초과

n = int(input())
t = []
orgin = []

for i in range(n):
    a, b = map(int, input().split())
    t += [b-a]
    orgin += [a-b]

def calc(std, orgin):
    value = 0
    for i in orgin:
        m = i+std
        if m < 0:
            value -= (i + std)
            continue
        value += (i + std)
    return value


std = int(sum(t)/len(t))
value = calc(std, orgin)
end = (max(orgin) - min(orgin))//2

result = [value]
for i in range(1, end):
    result.append(calc(std+i, orgin))
    result.append(calc(std-i, orgin))

print(result.count(min(result)))