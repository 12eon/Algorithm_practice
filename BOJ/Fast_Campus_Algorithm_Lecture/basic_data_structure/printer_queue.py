# 데이터 개수가 적기 때문에 append, pop으로 가능
test = int(input())
for _ in range(test):
    cnt, j = map(int, input().split())
    num = list(map(int, input().rstrip().split()))
    n = [(x,i) for i,x in enumerate(num)]

    result = 0
    for _ in range(cnt):
        m = max(n, key=lambda x : x[0])[0] # 우선순위 기준
        while n[0][0] != m:
            n.append(n.pop(0)) # 뒤로
        result += 1
        if n[0][1] == j:
            print(result)
            break
        else:
            n.pop(0)