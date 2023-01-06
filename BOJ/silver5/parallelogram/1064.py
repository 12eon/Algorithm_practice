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

    lengths = [distance[0]+distance[1], distance[1]+distance[2], +distance[0]+distance[2]]
    # 가장 긴 선으로 만든 길이 - 가장 짧은 선으로 만든 길이
    return (max(lengths)*2 - min(lengths)*2)

print(calc_diff(length, point2))