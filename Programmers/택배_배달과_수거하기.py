# 초기 : while로 1개씩 처리 -> 시간초과
# 해결 : cnt가 끊어지는 부분

def solution(cap, n, deliveries, pickups):
    d_val, p_val = 0,0
    answer = 0
    for i in range(n):
        d_val += deliveries[n-i-1]
        p_val += pickups[n-i-1]
        while p_val > 0 or d_val > 0:
        # 값이 시작되는 경우(0 -> 0 초과), cap 값을 초과한 경우 탐색(값-cap > 0)
        # while : 해당 위치에 처리 값이 많으면, 한번 더해진 경우에 처리량 > cnt
            d_val -= cap
            p_val -= cap
            answer += 2 * (n-i)
            print(d_val, p_val, n-i)
        print(d_val, p_val, n-i)
    return answer
