# KCPC

x = int(input())
for _ in range(x):
    log = []
    n,k,t,m = map(int, input().split())

    # 최종 점수, 제출 횟수, 최종 시간(순 sort), 팀번호
    cmp = [[0,0,0,i] for i in range(n+1)]
    score = [[0]*k for _ in range(n+1)]

    for i in range(m):
        tid, j, s = list(map(int, input().split()))
        cmp[tid][2] = i+1
        cmp[tid][1] += 1
        score[tid][j-1] = max(score[tid][j-1], s)

    for i in range(1, n+1):
        cmp[i][0] = sum(score[i])
    cmp.remove([0,0,0,0])

    cmp.sort(key = lambda x : (-x[0], x[1], x[2]))

    for i in range(n):
        if cmp[i][3] == t:
            print(i+1)
            break
