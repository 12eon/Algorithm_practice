n = int(input())
score = []
for i in range(n):
    std, k, e, m = input().split() # 타입이 다른 경우는 나눠서 받기
    score.append([std, int(k), int(e), int(m)])

score.sort(key = lambda x :(-x[1], x[2], -x[3], x[0]))
for s in score:
    print(s[0])
