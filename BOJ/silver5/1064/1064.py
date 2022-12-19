# 실패

import math

# 거리 계산을 위해서 3개 점 중 2가지 선택 -> 조합
# 조합 : yield 제너레이터 이용
def combinations(array, r):
    for i in range(len(array)):
        if r == 1: # 종료
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next


# 평행사변형
point = list(map(int, input().split()))
length = len(point)//2

point2 = []
for i in range(length):
    point2.append([point[2*i], point[2*i+1]])

def calc_diff(length, point2):
    comb = []
    for c in combinations(range(length), 2):
        comb.append(c)

    # 세 점 사이의 거리 계산
    distance = []
    for m, n in comb:
        #print([m, n], end = " ")
        distance.append(
            math.sqrt((point2[m][0] - point2[n][0])**2
                      + (point2[m][1] - point2[n][1])**2))
        #print(distance[-1])

    # 가장 긴 선으로 만든 길이 - 가장 짧은 선으로 만든 길이
    return 2*(max(distance) - min(distance))

# 예외
if point2[1][0] != point2[0][0] and point2[2][0] != point2[1][0]:
    m1 = (point2[1][1]-point2[0][1]) / (point2[1][0]-point2[0][0])
    m2 = (point2[2][1]-point2[1][1]) / (point2[2][0]-point2[1][0])
    if m1 == m2:
        print(-1.0)
    else:
        print(calc_diff(length, point2))
else:
    print(calc_diff(length, point2))