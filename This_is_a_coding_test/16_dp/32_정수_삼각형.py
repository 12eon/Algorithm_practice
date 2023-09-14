from collections import deque

h = int(input())
q = deque([[int(input()), 0]])

for y in range(h-1):
    num = list(map(int, input().split()))
    for j in range(len(q)):
        v, dx = q.popleft()
        for x in range(dx, dx+2):
            q.append([v+num[x], x])
        #print(q)

print(max(q)[0])