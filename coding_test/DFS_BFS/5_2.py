# 미로 탈출

from collections import deque

n,m = map(int, input().split())
miro = []
for j in range(n):
    miro.append([int(x) for x in list(input().rstrip())])

box = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs(q,v):
    result = 0
    while q :
        cd_q = deque([]) # 최단 거리를 위해
        while q :
            p = q.popleft()
            if p == [n-1,m-1]:
                break
            i = 0
            while i < 4:
                dy = p[0] + box[i][0]
                dx = p[1] + box[i][1]
                if dy < 0 or dy >= n or dx < 0 or dx >= m:
                    i += 1
                    continue
                if miro[dy][dx] == 1 and v[dy][dx] == 0:
                    cd_q.append([dy,dx])
                    v[dy][dx] = 1
                    # 2중 while 대신에 최단 거리 기록 -> miro[n-1][m-1] 출력
                    """
                    miro[dy][dx] = miro[p[0]][p[1]] + 1
                    """

                i += 1
        q = cd_q
        result += 1
    return result

v = [[0 for _ in range(m)] for _ in range(n)]
v[0][0] = 1
q = deque([[0,0]])

print(bfs(q,v))
