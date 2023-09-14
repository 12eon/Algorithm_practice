m, n = map(int, input().split())
v = []
for _ in range(m):
    v.append(int(input()))
v.sort()

start = 1
end = v[-1] - v[0]

result = 0
while start <= end :
    diff = (end+start)//2
    i = v[0]
    cnt = 1 # 시작 값
    for j in range(1, m):
        if v[j] - i >= diff:
            i = v[j]
            cnt += 1
    if cnt >= n:
        result = diff
        start = diff+1
    else:
        end = diff-1
print(result)