from collections import deque

N = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
check = [[0]*N for _ in range(N)] # 필수!

def check_valid(y,x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def dfs(sy, sx): # 재귀!
    # 끝내는 조건

    for i in range(4):
        y = sy + dy[i]
        x = sx + dx[i]
        if check_valid(y, x): # 미방문
            # 방문 여부 표시
            dfs(y,x)

def bfs(sy, sx):
    q = deque([(sy,sx)])
    # 끝내는 조건

    while q:
        v = q.popleft()
        for i in range(4):
            y = v[0] + dy[i]
            x = v[1] + dx[i]
            if check_valid(y,x): # 미방문
                # 방문 여부 표시
                q.append((y,x))
