# 무지의 먹방 라이브

import heapq


def solution(food_times, k):
    answer = -1
    food_num = len(food_times)

    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1)) # 우선순위 q

    previous = 0 # 이전 값
    while h:
        t = (h[0][0] - previous) * food_num # h[0][0] = 가장 작은 음식 양
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        else:
            h.sort(key=lambda x: x[1])
            answer = h[k % food_num][1] # 음식을 다 먹기 위한 시간보다 k가 큰 경우
            break
    return answer