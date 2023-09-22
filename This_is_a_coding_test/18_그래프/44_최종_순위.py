from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    # 작년 순위
    n = int(input())
    pre = list(map(int, input().split()))
    cnt = [-1]*(n+1)
    link = [[] for _ in range(n + 1)]
    for i in range(n):
        link[pre[i]] = pre[i + 1:] # 뒤의 링크들 담기
        cnt[pre[i]] = i # 링크 개수

    # 링크 교체
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if a in link[b]:
            link[b].remove(a)
            link[a].append(b)
            cnt[a] -= 1
            cnt[b] += 1
        else:
            link[a].remove(b)
            link[b].append(a)
            cnt[b] -= 1
            cnt[a] += 1

    # 시작 노드
    q = deque()
    for i in range(1, n + 1):
        if cnt[i] == 0:
            q.append(i)
    if not q:
        # 시작 노드 부재, 사이클
        print("IMPOSSIBLE")
        continue

    # 위상 정렬
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for i in link[v]:
            cnt[i] -= 1
            if cnt[i] == 0:
                q.append(i) # 본인이 가진 노드가 없는 경우

    if sum(cnt) > -1: # 사이클 존재
        print("IMPOSSIBLE")
    else:
        result = ''
        for a in ans:
            result += str(a)+' '
        print(result)