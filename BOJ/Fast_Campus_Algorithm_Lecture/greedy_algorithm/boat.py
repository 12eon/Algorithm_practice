import sys

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
    print(-1)
else:
    positions = [0] * n
    checked = [False] * m
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)

    result = 0
    count = 0
    while True:
        if count == len(boxes):
            break
        for i in range(n): # 모든 크레인에 대하여 각각 처리
            while positions[i] < len(boxes):
                # 아직 안 옮긴 박스 중에서, 옮길 수 있는 박스를 만날 때까지 반복
                if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                    checked[positions[i]] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        result += 1
    print(result)